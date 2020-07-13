import cx_Freeze
executables = [cx_Freeze.Executable("Turbo.py")]

cx_Freeze.setup(
    name="Turbo",
    options={"build_exe": {"packages":["pygame"],
    			"include_files":["image/","audio/"]}},
    executables = executables

    )