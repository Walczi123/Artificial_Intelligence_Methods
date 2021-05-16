if __name__ == "__main__":
    runGame()

    # # Binding, setting
    g.screen.bind("<Button-1>", clickHandle)
    g.screen.bind("<Key>", keyHandle)
    g.screen.focus_set()

    # Run forever
    g.root.wm_title("Not othello")
    g.root.mainloop()
