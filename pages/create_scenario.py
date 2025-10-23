"""Create Scenario Page - Interface for designing custom storytelling scenarios."""

import pygame

class CreateScenarioPage:
    """Page for creating and editing storytelling scenarios."""
    
    def __init__(self, app):
        self.app = app
        self.font_title = pygame.font.SysFont('Arial', 36, bold=True)
        self.font_normal = pygame.font.SysFont('Arial', 20)
        self.font_button = pygame.font.SysFont('Arial', 18)
        
        # Colors
        self.title_color = (30, 30, 50)
        self.text_color = (60, 60, 80)
        self.button_color = (70, 130, 180)
        self.button_hover_color = (100, 150, 200)
        self.button_text_color = (255, 255, 255)
        self.input_color = (255, 255, 255)
        self.input_border_color = (200, 200, 200)
        
        # UI Elements
        self.back_button = pygame.Rect(50, 50, 100, 40)
        self.save_button = pygame.Rect(400, 650, 224, 50)
        
        self.scenario_name = ""
        self.scenario_description = ""
        self.active_input = None
        self.hovered_button = None
    
    def handle_event(self, event):
        """Handle user input events."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            
            if self.back_button.collidepoint(mouse_pos):
                self.app.navigate_to("home")
            elif self.save_button.collidepoint(mouse_pos):
                # Save scenario logic would go here
                print(f"Scenario saved: {self.scenario_name}")
        
        elif event.type == pygame.KEYDOWN:
            if self.active_input and event.key == pygame.K_BACKSPACE:
                if self.active_input == "name":
                    self.scenario_name = self.scenario_name[:-1]
                elif self.active_input == "description":
                    self.scenario_description = self.scenario_description[:-1]
            elif self.active_input and event.unicode.isprintable():
                if self.active_input == "name":
                    self.scenario_name += event.unicode
                elif self.active_input == "description":
                    self.scenario_description += event.unicode
    
    def update(self):
        """Update page state."""
        mouse_pos = pygame.mouse.get_pos()
        self.hovered_button = None
        
        if self.back_button.collidepoint(mouse_pos):
            self.hovered_button = "back"
        elif self.save_button.collidepoint(mouse_pos):
            self.hovered_button = "save"
    
    def render(self, screen):
        """Render the create scenario page."""
        # Title
        title_text = self.font_title.render("Create Scenario", True, self.title_color)
        screen.blit(title_text, (50, 120))
        
        # Back button
        back_color = self.button_hover_color if self.hovered_button == "back" else self.button_color
        pygame.draw.rect(screen, back_color, self.back_button, border_radius=5)
        back_text = self.font_button.render("← Back", True, self.button_text_color)
        back_rect = back_text.get_rect(center=self.back_button.center)
        screen.blit(back_text, back_rect)
        
        # Instructions
        instruction_text = self.font_normal.render("Design your custom scenario with characters and events", True, self.text_color)
        screen.blit(instruction_text, (50, 180))
        
        # Input fields (simplified representation)
        name_label = self.font_normal.render("Scenario Name:", True, self.text_color)
        screen.blit(name_label, (50, 250))
        
        desc_label = self.font_normal.render("Description:", True, self.text_color)
        screen.blit(desc_label, (50, 350))
        
        # Save button
        save_color = self.button_hover_color if self.hovered_button == "save" else self.button_color
        pygame.draw.rect(screen, save_color, self.save_button, border_radius=10)
        save_text = self.font_button.render("Save Scenario", True, self.button_text_color)
        save_rect = save_text.get_rect(center=self.save_button.center)
        screen.blit(save_text, save_rect)
