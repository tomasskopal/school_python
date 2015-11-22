#!/usr/bin/env python
# with this configuration I can run program just with using ./main.py .Without 'python' at the beginning

__author__ = 'tomasskopal'

from optparse import OptionParser  # http://www.saltycrane.com/blog/2009/09/python-optparse-example/
from ConfigParser import SafeConfigParser
import shlex
configParser = SafeConfigParser()

# TODO : switch url to some kind of Set. Array allows duplicate values.
def main():
    # parse command line parameters
    parser = OptionParser(usage="usage: %prog [options] file file",
                          version="%prog 1.0")
    parser.add_option("-v",
                      action="store_true",
                      default=False)
    parser.add_option("-u", action='append')  # allow multiplicity
    parser.add_option("-H", "--host")
    parser.add_option("-p")
    (options, args) = parser.parse_args()

    if len(args) != 2:
        parser.error("wrong number of arguments")
        return

    # set command line parameters into the result dictionary. If something missing value is None
    result = dict([
        ("verbose", options.v),
        ("host", options.host),
        ("port", options.p),
        ("url", options.u)
    ])

    # parse configuration files. Url must be concatenated
    configParser.read(args[0])
    for name, value in configParser.items('server'):
        if name == 'url':
            value = shlex.split(value)
        if result[name] is None:
            result[name] = value
            continue
        if name == 'url' and result['url'] is not None:
            result['url'] = result['url'] + value


    configParser.read(args[1])
    for name, value in configParser.items('server'):
        if name == 'url':
            value = shlex.split(value)
        if result[name] is None:
            result[name] = value
            continue
        if name == 'url' and result['url'] is not None:
            result['url'] = result['url'] + value

    print result

if __name__ == '__main__':
    main()