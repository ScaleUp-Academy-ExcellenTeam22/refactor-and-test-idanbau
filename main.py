import random
import pygame

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15


class Snake:
    def __init__(self):
        pygame.init()
        self.font_style = pygame.font.SysFont("bahnschrift", 25)
        self.score_font = pygame.font.SysFont("comicsansms", 35)
        self.display = pygame.display.set_mode((dis_width, dis_height))
        pygame.display.set_caption('Snake Game by Edureka')
        self.game_over = False
        self.game_close = False
        self.current_location = [dis_width / 2, dis_height / 2]
        self.next_move = [0, 0]
        self.snake_list = []
        self.length_of_snake = 1
        self.food = self.get_random_food()

    def show_score(self, score_font, score):
        """
        Show score function
        :param score_font: The specific font to show
        :param score: Current score
        """
        value = score_font.render("Your Score: " + str(score), True, yellow)
        self.display.blit(value, [0, 0])

    def our_snake(self, snake_block_arg, snake_list):
        """
        Display our snake
        :param snake_block_arg: Snake size
        :param snake_list: List of snake cells
        """
        for cell in snake_list:
            pygame.draw.rect(self.display, black, [cell[0], cell[1], snake_block_arg, snake_block_arg])

    def message(self, font_style, msg, color):
        """
        Display current message in the game
        :param font_style: Message font size
        :param msg: msg string
        :param color: Message color
        """
        msg = font_style.render(msg, True, color)
        self.display.blit(msg, [dis_width / 6, dis_height / 3])

    @staticmethod
    def is_game_ended(snake_head, snake_list):
        """
        Check if game is ended or not
        :param snake_head: Current snake location
        :param snake_list: current snake
        :return: if the snake is hit itself
        """
        return any(x == snake_head for x in snake_list[:-1])

    @staticmethod
    def is_out_of_boarders(current_location: []):
        """
        Check if snake is out of game boarders
        :param current_location: Current snake location
        :return: True if snake is out of the game boarder or false
        """
        return current_location[0] >= dis_width or current_location[0] < 0 \
               or current_location[1] >= dis_height or current_location[1] < 0

    @staticmethod
    def get_random_food():
        """
        Get Random food location
        :return: list represents X,Y of the food location
        """
        return [round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0,
                round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0]

    def game_loop(self):
        """
        Main Game loop which the game is occurred here.
        """
        while not self.game_over:
            while self.game_close:
                self.display.fill(blue)
                self.message(self.font_style, "You Lost! Press C-Play Again or Q-Quit", red)
                self.show_score(self.score_font, self.length_of_snake - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            self.game_over = True
                            self.game_close = False
                        elif event.key == pygame.K_c:
                            self.game_loop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.next_move = [-snake_block, 0]
                    elif event.key == pygame.K_RIGHT:
                        self.next_move = [snake_block, 0]
                    elif event.key == pygame.K_UP:
                        self.next_move = [0, -snake_block]
                    elif event.key == pygame.K_DOWN:
                        self.next_move = [0, snake_block]

            if self.is_out_of_boarders(self.current_location):
                self.game_close = True
            self.current_location[0] += self.next_move[0]
            self.current_location[1] += self.next_move[1]
            self.display.fill(blue)
            pygame.draw.rect(self.display, green, [self.food[0], self.food[1], snake_block, snake_block])
            self.snake_list.append([self.current_location[0], self.current_location[1]])
            if len(self.snake_list) > self.length_of_snake:
                del self.snake_list[0]

            if self.is_game_ended(self.current_location, self.snake_list):
                self.game_close = True

            self.our_snake(snake_block, self.snake_list)
            self.show_score(self.score_font, self.length_of_snake - 1)

            pygame.display.update()

            if self.current_location == self.food:
                self.food = self.get_random_food()
                self.length_of_snake += 1
            clock.tick(snake_speed)

        pygame.quit()
        quit()


if __name__ == "__main__":
    Snake().game_loop()
