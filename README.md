# Game Library !!
Features Tic-Tac-Toe, Hangman, and Wordle!!

### TIC_TAC_TOE ADJUSTMENTS
- [x] Translate the tic_tac_toe visuals to the center of the screen:  
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

- [x] Adjust the clicking coordinates:
    - The OG tic tac toe code converts the coordinates of the click into a single digit number that coresponds to a position on an array/board.
    - I adjusted this by manually looking for the x pos of the mouse to be in a certain range.