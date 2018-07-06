import allure

class Test_001:

    @allure.step(title="第一步测试")
    def test_001(self):
        @allure.attach("姓名","我是项目描述")
        print("woshiyizhixiaozhu")

    @allure.step(title="第二步测试")
    @allure.attach("写别", "我是性别描述")
    def test_002(self):
        print("我是小刘")

    @allure.step(title="第二步测试")
    @allure.attach("姓", "我是属性描述")
    def test_003(self):
        print("闹闹")
