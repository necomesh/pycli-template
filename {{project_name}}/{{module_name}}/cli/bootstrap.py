from dotenv import load_dotenv
import fire
from loguru import logger

load_dotenv()

class CLI:
    pass
    
def main():
    """主入口函数"""
    fire.Fire(CLI)

