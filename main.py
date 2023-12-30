from build import ActionBuilder, CollectActions

if __name__ == "__main__":
    actionBuilder = ActionBuilder()
    app = CollectActions(actionBuilder)
    app.mainloop()
