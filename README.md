# moravecs_method
Moravec's Corner Detector

Moravec's corner detector functions by considering a local
window in the image, and determining the average changes
of image intensity that result from shifting the window by
a small amount in various directions. Three cases need to
be considered:

A. If the windowed image patch is flat (ie. approximately
constant in intensity), then all shifts will result in only
a small change;

B. If the window straddles an edge, then a shift along the
edge will result in a small change, but a shift
perpendicular to the edge will result in a large change;

C. If the windowed patch is a corner or isolated point, then
all shifts will result in a large change. A corner can
thus be detected by finding when the minimum change
produced by any of the shifts is large.

![alt text](demo.gif)
