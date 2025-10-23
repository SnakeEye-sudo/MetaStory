"""View Simulation Page - Real-time visualization of active scenarios."""

import pygame
import math
import random

class ViewSimulationPage:
    """Page for viewing and interacting with running simulations."""
    
    def __init__(self, app):
        self.app = app
        self.font_title = pygame.font.SysFont('Arial', 36, bold=True)
        self.font_normal = pygame.font.SysFont('Arial', 18)
        self.font_button = pygame.font.SysFont('Arial', 18)
        
        # Colors
        self.title_color = (30, 30, 50)
        self.text_color = (60, 60, 80)
        self.button_color = (70, 130, 180)
        self.button_hover_color = (100, 150, 200)
        self.button_text_color = (255, 255, 255)
        self.sim_bg_color = (250, 250, 250)
        self.entity_color = (220, 100, 100)
        
        # UI Elements
        self.back_button = pygame.Rect(50, 50, 100, 40)
        self.sim_area = pygame.Rect(50, 150, 924, 500)
        
        # Simulation state
        self.entities = []
        self.time_step = 0
        self.is_running = False
        self.hovered_button = None
        
        # Initialize some demo entities
        for i in range(5):
            self.entities.append({
                "x": random.randint(100, 900),
                "y": random.randint(200, 600),
                "vx": random.uniform(-2, 2),
                "vy": random.uniform(-2, 2),
                "radius": 15
            })
    
    def handle_event(self, event):
        """Handle user input events."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            
            if self.back_button.collidepoint(mouse_pos):
                self.app.navigate_to("home")
    
    def update(self):
        """Update simulation state."""
        mouse_pos = pygame.mouse.get_pos()
        self.hovered_button = None
        
        if self.back_button.collidepoint(mouse_pos):
            self.hovered_button = "back"
        
        # Update entity positions
        for entity in self.entities:
            entity["x"] += entity["vx"]
            entity["y"] += entity["vy"]
            
            # Bounce off walls
            if entity["x"] < self.sim_area.left + entity["radius"]:
                entity["x"] = self.sim_area.left + entity["radius"]
                entity["vx"] *= -1
            elif entity["x"] > self.sim_area.right - entity["radius"]:
                entity["x"] = self.sim_area.right - entity["radius"]
                entity["vx"] *= -1
            
            if entity["y"] < self.sim_area.top + entity["radius"]:
                entity["y"] = self.sim_area.top + entity["radius"]
                entity["vy"] *= -1
            elif entity["y"] > self.sim_area.bottom - entity["radius"]:
                entity["y"] = self.sim_area.bottom - entity["radius"]
                entity["vy"] *= -1
        
        self.time_step += 1
    
    def render(self, screen):
        """Render the view simulation page."""
        # Title
        title_text = self.font_title.render("View Simulation", True, self.title_color)
        screen.blit(title_text, (50, 120))
        
        # Back button
        back_color = self.button_hover_color if self.hovered_button == "back" else self.button_color
        pygame.draw.rect(screen, back_color, self.back_button, border_radius=5)
        back_text = self.font_button.render("← Back", True, self.button_text_color)
        back_rect = back_text.get_rect(center=self.back_button.center)
        screen.blit(back_text, back_rect)
        
        # Simulation area
        pygame.draw.rect(screen, self.sim_bg_color, self.sim_area)
        pygame.draw.rect(screen, (200, 200, 200), self.sim_area, 2)
        
        # Render entities
        for entity in self.entities:
            pygame.draw.circle(screen, self.entity_color, (int(entity["x"]), int(entity["y"])), entity["radius"])
        
        # Status text
        status_text = self.font_normal.render(f"Time Step: {self.time_step}", True, self.text_color)
        screen.blit(status_text, (60, 670))
