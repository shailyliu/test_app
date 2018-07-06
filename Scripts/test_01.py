import allure

class Test_001:

    @allure.step(title="第一步测试")
    def test_001(self):
        print("woshiyizhixiaozhu")

    @allure.step(title="第二步测试")
    def test_002(self):
        print("我是小刘")

    @allure.step(title="第二步测试")
    def test_003(self):
        print("闹闹")
