

c
    def setup(self):
        pass
    def setUp(self):
        print("\nsetup")
    def tearDown(selfself):
        print("\nteardown")
    def test_add(self):
        self.assertEqual(loki.add(40,20),60)

        print("\nteardown")
    def test_sub(self):
        self.assertEqual(loki.sub(40, 20),20)

    def test_equal(self):
        self.assertEqual(10,10)

if __name__=='__main__':
    unittest.main()
