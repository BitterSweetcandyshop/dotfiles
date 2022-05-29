/* center radius (pixels) */
#define C_RADIUS 425
/* center line thickness (pixels) */
#define C_LINE 0
/* outline color */
#define OUTLINE #ffffff
/* Amplify magnitude of the results each bar displays */
#define AMPLIFY 250
/* Angle (in radians) for how much to rotate the visualizer */
#define ROTATE (PI / -8.5)
/* Whether to switch left/right audio buffers */
#define INVERT 1
/* Whether to fill in the space between the line and inner circle */
#define C_FILL 1
/* Whether to apply a post-processing image smoothing effect
   1 to enable, 0 to disable. Only works with `xroot` transparency,
   and improves performance if disabled. */
#define C_SMOOTH 1

/* Gravity step, overrude frin `smooth_parameters.glsl` */
#request setgravitystep 6.0

/* Smoothing factor, override from `smooth_parameters.glsl` */
#request setsmoothfactor 0.01
