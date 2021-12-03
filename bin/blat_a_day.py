#!/usr/bin/env python3

from sys import argv, stderr, exit
import subprocess

TEMPLATE = '''diff --git a/teagles_advent_2021/day_{day}/__init__.py b/teagles_advent_2021/day_{day}/__init__.py
new file mode 100644
index 0000000..e69de29
diff --git a/teagles_advent_2021/day_{day}/lib.py b/teagles_advent_2021/day_{day}/lib.py
new file mode 100644
index 0000000..e990c97
--- /dev/null
+++ b/teagles_advent_2021/day_{day}/lib.py
@@ -0,0 +1,2 @@
+def noop():
+    return None
diff --git a/teagles_advent_2021/day_{day}/pt1.py b/teagles_advent_2021/day_{day}/pt1.py
new file mode 100644
index 0000000..b43c3b8
--- /dev/null
+++ b/teagles_advent_2021/day_{day}/pt1.py
@@ -0,0 +1,11 @@
+import sys
+
+from .lib import noop
+
+
+def main():
+    print()
+
+
+if __name__ == '__main__':
+    main()
diff --git a/teagles_advent_2021/day_{day}/pt2.py b/teagles_advent_2021/day_{day}/pt2.py
new file mode 100644
index 0000000..b43c3b8
--- /dev/null
+++ b/teagles_advent_2021/day_{day}/pt2.py
@@ -0,0 +1,11 @@
+import sys
+
+from .lib import noop
+
+
+def main():
+    print()
+
+
+if __name__ == '__main__':
+    main()
diff --git a/test/day_{day}/__init__.py b/test/day_{day}/__init__.py
new file mode 100644
index 0000000..e69de29
diff --git a/test/day_{day}/test_lib.py b/test/day_{day}/test_lib.py
new file mode 100644
index 0000000..8a1b41d
--- /dev/null
+++ b/test/day_{day}/test_lib.py
@@ -0,0 +1,14 @@
+import unittest
+
+from teagles_advent_2021.day_{day}.lib import noop
+
+
+class TestDay{day}Lib(unittest.TestCase):
+    def test_expectations(self):
+        expectation = None
+        reality = noop()
+        self.assertEqual(expectation, reality)
+
+
+if __name__ == '__main__':
+    unittest.main()
diff --git a/test/day_{day}/test_pt1.py b/test/day_{day}/test_pt1.py
new file mode 100644
index 0000000..a93f94a
--- /dev/null
+++ b/test/day_{day}/test_pt1.py
@@ -0,0 +1,16 @@
+import unittest
+
+from test.std_test_utils import STDIOTest
+from teagles_advent_2021.day_{day}.pt1 import main
+
+TEST_INPUT = """
+"""
+
+
+class TestDay{day}Part1(STDIOTest):
+    def test_with_sample_input(self):
+        self.assert_stdin_n_out(main, TEST_INPUT, "\\n")
+
+
+if __name__ == '__main__':
+    unittest.main()
diff --git a/test/day_{day}/test_pt2.py b/test/day_{day}/test_pt2.py
new file mode 100644
index 0000000..65d6f86
--- /dev/null
+++ b/test/day_{day}/test_pt2.py
@@ -0,0 +1,16 @@
+import unittest
+
+from test.std_test_utils import STDIOTest
+from teagles_advent_2021.day_{day}.pt2 import main
+
+TEST_INPUT = """
+"""
+
+
+class TestDay{day}Part2(STDIOTest):
+    def test_with_sample_input(self):
+        self.assert_stdin_n_out(main, TEST_INPUT, "\\n")
+
+
+if __name__ == '__main__':
+    unittest.main()
'''

if len(argv) != 2:
    print('Must supply a day number.', file=stderr)
    exit(1)

subprocess.run(["git", "apply", "-"], stdout=subprocess.PIPE, text=True, input=TEMPLATE.format(day=argv[1]))
subprocess.run(["git", "add", f"teagles_advent_2021/day_{argv[1]}/", f"test/day_{argv[1]}/"])
