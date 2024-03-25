import json

class CommandHandler:
    def __init__(self):
        self.actions = {}

    def register_command(self, command_id, command_text, action):
        self.actions[(command_id, command_text)] = action

    def execute_command(self, command_id, command_text=None):
        action_key = (command_id, command_text) if command_text else command_id
        if action_key in self.actions:
            self.actions[action_key]()
        else:
            print(f"No action defined for command: {command_text} with ID: {command_id}")

    def parse_data(self, data):
        command = data.get("command", "None")
        id = data.get("id", 0)
        xmos_status = data.get("xmos_status", False)  # 예제에서는 사용하지 않지만 추출된 데이터
        self.execute_command(id, command)
