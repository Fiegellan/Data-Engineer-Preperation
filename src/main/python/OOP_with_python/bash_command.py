# == Summary:
#
# This class takes a list of commands and breaks them into 4 commands:
#           DEPEND, INSTALL, REMOVE, LIST
#
# == Usage: to quickly install and see what dependencies there are.
# == Input Parameters: a list of commands, with DEPENDS coming before the INSTALL
# == Enhancements: Could create a graph/tree visualization of what depends on what.
# == Not completed: Installing dependencies if not already installed,
#    simply add a loop through dictionary based on the key and check if all values are installed, if not install

"""
I built this script on the IDE as the recruiter recommended.  I valided in PyCharm with the proper output.
If input would be a text file, just use the open() function and it would create the list and loop through.
Thanks for your time! I appreciated the challenge.
"""


class Aloha1:

    # global variables, keeping track of dependencies and installed items

    installed_items = []
    depend_dic = {}

    def __init__(self, list):
        """
        First take the input list and sort it based on the commandsand have it sent to the various correct locations
        """

        self.sort_input(list)

    def sort_input(self, list):
        """
        Takes the first word of each item in the list and matches it (case sensitve) to the proper function.
        Pops the first number value out and echo's END
        """

        list.pop(0)
        for i in list:

            # check for the end here if the split is > 1 else check for end else through error

            if i.split(' ')[0] == 'DEPEND':
                self.depend(i)
            elif i.split(' ')[0] == 'INSTALL':
                self.install(i)
            elif i.split(' ')[0] == 'REMOVE':
                self.remove(i)
            elif i.split(' ')[0] == 'LIST':
                self.list(i)
            elif i.split(' ')[0] == 'END':
                print 'END'
            else:
                print i.split(' ')[0] + 'is an invalid command'

    def depend(self, depend_item):

        # takes the list and cuts it into what the first value depends on
        # Then takes the array of values depend and checks it against the global dictonary
        # The set of keys are returned and vetted to see if theres and internal depency
        # If there is an internal depency, there throws an error, if not it echos the depend
        # I wasn't sure if the echo needed to have extra spaces rmoved so I kept them as is.

        depends_dictioanry = {}
        command = depend_item.split(' ')
        command = [x for x in command if x]
        i = 2
        dependent_items = []

        while i < len(command):

            # print command[i]

            dependent_items.append(command[i])
            i = i + 1

        set_keys = self.check_dependency(dependent_items)
        values_dependent = []
        for i in dependent_items:
            if i in set_keys:
                values_dependent.append(i)
                count = 0
            else:
                count = 1

        if count == 0:
            print values_dependent[0] + ' depends on ' \
                + values_dependent[1], ' ignoring command'
        else:
            print depend_item
            depends_dictioanry[command[1]] = dependent_items
        self.depend_dic.update(depends_dictioanry)

    def check_dependency(self, depend_check):

        # Used to check depencies within depencies.
        # This returns a set of keys that include the depency and will be used to validate in the depend function

        check_keys = []
        for (key, value) in self.depend_dic.iteritems():
            for i in value:
                for z in depend_check:
                    if i == z:
                        check_keys.append(key)

        return set(check_keys)

    def install(self, install_item):

        # Takes the list of installs and checks if it's already installed.
        # If so it prints it's already been installed and moves on, otherwise it installs
        # Echos the command either way then the error or installs

        print install_item
        command = install_item.split(' ')
        if command[1] not in self.installed_items:
            self.installed_items.append(command[1])
            print 'Installing ' + command[1]
        else:
            print command[1] + ' is already installed'

    def remove(self, remove_item):

        # gather items in the dictonary for the remove item.
        # Then remove all items and all dictionary values.
        # If theres an error, it says the item is still needed.
        # This still needs to be tested. I'm not sold on it and would spend more time here

        print remove_item
        command = remove_item.split(' ')[1]

        if command in self.installed_items:
            self.installed_items.remove(command)
            for i in self.depend_dic.get(command):

                # print i

                if i not in self.installed_items:
                    print command + ' is still needed'
        else:
            print 'not a valid command'

        # print self.installed_items

    def list(self, list_item):

        # simple - just print the list of installed items in a row

        print 'LIST'
        for i in self.installed_items:
            print i


def main():
    """

    where I created the test cases to run and validate against the requirments
    """

    # list2 = ['DEPEND      TELNET TCPIP NETCARD','DEPEND  TCPIP NETCARD', 'INSTALL NETCARD', 'REMOVE NETCARD', 'LIST','DEPEND      TELNET TCPIP NETCARD', 'END']
    # list_depend = ['DEPEND      TELNET TCPIP NETCARD', 'DEPEND  TCPIP NETCARD', 'DEPEND  TCPIP NETCARD']
    # list_install = ['22','DEPEND      TELNET TCPIP NETCARD','INSTALL NETCARD','INSTALL TCPIP', 'INSTALL TELNET', 'LIST', 'REMOVE TELNET','INSTALL foo', 'LIST', 'END']

    test = [
        '22',
        'DEPEND    TELNET TCPIP NETCARD',
        'DEPEND TCPIP NETCARD',
        'DEPEND NETCARD TCPIP',
        'DEPEND DNS TCPIP NETCARD',
        'DEPEND BROWSER TCPIP HTML',
        'INSTALL NETCARD',
        'INSTALL TELNET',
        'INSTALL foo',
        'REMOVE NETCARD',
        'INSTALL BROWSER',
        'INSTALL DNS',
        'LIST',
        'INSTALL TELNET',
        'END',
        ]
    test2 = (
        'REMOVE TELNET',
        'REMOVE NETCARD',
        'REMOVE DNS',
        'REMOVE NETCARD',
        'INSTALL NETCARD',
        'REMOVE TCPIP',
        'REMOVE BROWSER',
        'REMOVE TCPIP',
        'LIST',
        'END',
        )
    Aloha1(test)


if __name__ == '__main__':
    main()
