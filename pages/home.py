"""Home Page - Main navigation hub for MetaStory application."""

import pygame

class HomePage:
    """Home page with navigation buttons to different sections."""
    
    def __init__(self, app):
        self.app = app
        self.font_title = pygame.font.SysFont('Arial', 48, bold=True)
        self.font_button = pygame.font.SysFont('Arial', 24)
        
        # Colors
        self.title_color = (30, 30, 50)
        self.button_color = (70, 130, 180)
        self.button_hover_color = (100, 150, 200)
        self.button_text_color = (255, 255, 255)
        
        # Button definitions
        self.buttons = [
            {"text": "Create Scenario", "page": "create_scenario", "rect": pygame.Rect(312, 250, 400, 60)},
            {"text": "View Simulation", "page": "view_simulation", "rect": pygame.Rect(312, 330, 400, 60)},
            {"text": "Timeline", "page": "timeline", "rect": pygame.Rect(312, 410, 400, 60)}
        ]
        
        self.hovered_button = None
    
    def handle_event(self, event):
        """Handle user input events."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for button in self.buttons:
                if button["rect"].collidepoint(mouse_pos):
                    self.app.navigate_to(button["page"])
    
    def update(self):
        """Update page state."""
        mouse_pos = pygame.mouse.get_pos()
        self.hovered_button = None
        
        for i, button in enumerate(self.buttons):
            if button["rect"].collidepoint(mouse_pos):
                self.hovered_button = i
                break
    
    def render(self, screen):
        """Render the home page."""
        # Title
        title_text = self.font_title.render("MetaStory", True, self.title_color)
        title_rect = title_text.get_rect(center=(512, 120))
        screen.blit(title_text, title_rect)
        
        # Subtitle
        subtitle_font = pygame.font.SysFont('Arial', 20)
        subtitle_text = subtitle_font.render("Interactive Storytelling Simulation Platform", True, self.title_color)
        subtitle_rect = subtitle_text.get_rect(center=(512, 170))
        screen.blit(subtitle_text, subtitle_rect)
        
        # Buttons
        for i, button in enumerate(self.buttons):
            color = self.button_hover_color if i == self.hovered_button else self.button_color
            pygame.draw.rect(screen, color, button["rect"], border_radius=10)
            
            text_surface = self.font_button.render(button["text"], True, self.button_text_color)
            text_rect = text_surface.get_rect(center=button["rect"].center)
            screen.blit(text_surface, text_rect)
