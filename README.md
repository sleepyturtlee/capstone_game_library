# capstone_game_library

### TIC_TAC_TOE ADJUSTMENTS
[x] added these lines of code into the tic_tac_toe file:
    ```
         # copy everything from the scree(above) onto a temporary surface
        temp_surf = screen.copy()
        # cover the previous frame by filling in with white
        screen.fill(white)
        # copy everything over
        screen.blit(temp_surf, (350, 0))
        pygame.display.update()
        screen.blit(screen, (-350, 0))
    ```
    I put it inside the game loop!