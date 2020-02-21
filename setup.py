import cx_Freeze

executables = [cx_Freeze.Executable("Slither.py")]

cx_Freeze.setup(
	name="Slither",
	options={"build_exe":{"packages":["pygame"],"include_files":["apple.png","snakeHead.png"]}},
	description="Slither Game Tutorial",
	executables = executables
	)