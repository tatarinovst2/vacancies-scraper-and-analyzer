"""Creates random headers"""
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem


def get_headers() -> dict:
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/39.0.2171.95 Safari/537.36'}
    return headers


def get_random_headers() -> dict:
    """Creates random headers"""
    software_names = [SoftwareName.CHROME.value,
                      SoftwareName.ANDROID.value,
                      SoftwareName.SAFARI.value,
                      SoftwareName.FIREFOX.value]
    operating_systems = [OperatingSystem.WINDOWS.value,
                         OperatingSystem.LINUX.value,
                         OperatingSystem.MAC.value,
                         OperatingSystem.CHROMEOS.value]
    useragent_random = UserAgent(software_names=software_names,
                                 operating_systems=operating_systems,
                                 limit=100)

    return {'user-agent': useragent_random.get_random_user_agent(),
            'accept': '*/*', 'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'}
