from enum import Enum

class FuncEnum(Enum):
    @classmethod
    def get_names(cls) -> list[str]:
        return [member.name for member in cls]
    
    @classmethod
    def get_values(cls) -> list[str]:
        return [member.value for member in cls]
    
if __name__ == "__main__":
    TEST_ENUM = FuncEnum("TEST_ENUM", ["ONE", "TWO", "THREE"])
    print(TEST_ENUM.get_values())