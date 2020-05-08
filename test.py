import unittest
import os

# Interested only that the software is present. Version isn't important.
def version_output(input):
    one_dash = ["xterm"]
    if input in one_dash:
        cmd = '{0} -version'.format(input)
    else:
        cmd = '{0} --version'.format(input)
    string = os.popen(cmd).read().strip()
    return string.join(string.split(' ')[0:1])


# If any test fails the build fails due to an exit code unittest provides.
class TestVersions(unittest.TestCase):

    def test_bash(self):
        self.assertEqual(version_output('bash'), "GNU")

    def test_Emacs(self):
        self.assertEqual(version_output('emacs'), "GNU")

    def test_Git(self):
        self.assertEqual(version_output('git'), "git")

    def test_Nano(self):
        self.assertEqual(version_output('nano'), "GNU")

    def test_Python3(self):
        self.assertEqual(version_output('python3'), "Python")

    def test_Vim(self):
        self.assertEqual(version_output('vim'), "VIM")

    def test_XFCE_terminal(self):
        self.assertEqual(version_output("xfce4-terminal"), "xfce4-terminal")

    def test_Xvnc(self):
        self.assertEqual(version_output('x11vnc'), "x11vnc:")

if __name__ == '__main__':
    unittest.main()