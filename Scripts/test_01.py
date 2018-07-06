import allure,pytest

class Test_001:
    @pytest.allure.severity(pytest.allure.severity_level.normal)
    @allure.step(title="第一步测试")
    def test_001(self):
        allure.attach("姓名","我是项目描述")
        print("woshiyizhixiaozhu")

    @pytest.allure.severity(pytest.allure.severity_level.normal)
    @allure.step(title="第二步测试")
    def test_002(self):
        allure.attach("写别", "我是性别描述")
        print("我是小刘")

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    @allure.step(title="第二步测试")
    def test_003(self):
        allure.attach("姓", "我是属性描述")
        print("闹闹")
