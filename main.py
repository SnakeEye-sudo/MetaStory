"""MetaStory - Interactive Storytelling Simulation Platform

Main application entry point that initializes PyGame and manages page navigation.
"""

import pygame
import sys
from pages.home import HomePage
from pages.create_scenario import CreateScenarioPage
from pages.view_simulation import ViewSimulationPage
from pages.timeline import TimelinePage

# Initialize PyGame
pygame.init()

# Screen configuration
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("MetaStory - Interactive Storytelling Platform")

# Colors
BG_COLOR = (240, 240, 245)

# Frame rate
clock = pygame.time.Clock()
FPS = 60

class Application:
    """Main application class managing page navigation and state."""
    
    def __init__(self):
        self.screen = screen
        self.running = True
        self.current_page = "home"
        
        # Initialize pages
        self.pages = {
            "home": HomePage(self),
            "create_scenario": CreateScenarioPage(self),
            "view_simulation": ViewSimulationPage(self),
            "timeline": TimelinePage(self)
        }
    
    def navigate_to(self, page_name):
        """Navigate to a different page."""
        if page_name in self.pages:
            self.current_page = page_name
    
    def run(self):
        """Main application loop."""
        while self.running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                else:
                    # Pass events to current page
                    self.pages[self.current_page].handle_event(event)
            
            # Update current page
            self.pages[self.current_page].update()
            
            # Render
            self.screen.fill(BG_COLOR)
            self.pages[self.current_page].render(self.screen)
            
            pygame.display.flip()
            clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    app = Application()
    app.run()
