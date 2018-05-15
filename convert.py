import ffmpy

ff = ffmpy.FFmpeg(
    inputs={'Bastian Piano - level 1/Bastien Piano Basics Level 1 Piano No1 March On! (P6).mp4':None},
    outputs={'mpeg.mpeg': None}
    )

ff.run()


