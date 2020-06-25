import rclpy
from rclpy.node import Node

from module import module_pico

#from _msgs.msg import Command
from std_msgs.msg import String

class SoundSystem(Node):
    def __init__(self):
        super(SoundSystem, self).__init__('SoundSystem')

        self.create_subscription(
            String, '/chat',
            self.command_callback,
            10
        )

        self.senses_publisher = self.create_publisher(
            String,
            '/speak',
            10
        )

    # recieve a command {Command, Content}
    def command_callback(self, msg):

        self.command = []
        self.speak_wards = None
        self.command = msg.data.split(" ")

        if self.command[0].lower() == "please":
            self.command.pop(0)

        if self.command[0].lower() == "say" or self.command[0].lower() == "speak":
            if self.command[1].lower() == "that":
                del self.command[:2]
            else:self.command.pop(0)
            self.speak_wards  = self.command[0]
            for i in range(1,len(self.command)):
                self.speak_wards += " " + self.command[i]

        if self.command[0].lower() == "food":
            self.command.pop(0)
            self.speak_wards = self.command[0]
            for i in range(1, len(self.command)):
                self.speak_wards += " " + self.command[i]
            self.speak_wards = "Hello, I brought {} for you." \
                               " please take this plate, Thank you.".format(self.speak_wards)

        if self.speak_wards != None:
            if module_pico.speak(self.speak_wards)==1:
                self.senses_publisher(self.speak_wards)


    # Publish a result of an action
    def cerebrum_publisher(self, message):
        _trans_message = String()
        _trans_message.data = message

        self.senses_publisher.publish(_trans_message)
        # self.destroy_publisher(self.senses_publisher)

def main():
    rclpy.init()
    node = SoundSystem()
    rclpy.spin(node)


if __name__ == '__main__':
    main()
