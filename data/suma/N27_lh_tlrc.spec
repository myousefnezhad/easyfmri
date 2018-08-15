# delimits comments

# Creation information:
#     user    : christip
#     date    : Mon Dec 13 16:20:29 EST 2004
#     machine : varda
#     pwd     : /home/christip/data/subjects/colin/colin_FS2/SUMA
#     command : @SUMA_Make_Spec_FS -sid N27

# define the group
        Group = N27

# define various States
        StateDef = smoothwm
        StateDef = pial
        StateDef = inflated
        StateDef = occip.patch.3d
        StateDef = occip.patch.flat
        StateDef = full.patch.3d
        StateDef = full.patch.flat
        StateDef = sphere
        StateDef = white
        StateDef = sphere.reg

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = Ply
        FreeSurferSurface = lh.smoothwm.tlrc.ply
        LocalDomainParent = SAME
        SurfaceState = smoothwm
        EmbedDimension = 3

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = Ply
        FreeSurferSurface = lh.pial.tlrc.ply
        LocalDomainParent = lh.smoothwm.tlrc.ply
        SurfaceState = pial
        EmbedDimension = 3

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = FreeSurfer
        FreeSurferSurface = lh.inflated.asc
        LocalDomainParent = lh.smoothwm.tlrc.ply
        SurfaceState = inflated
        EmbedDimension = 3

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = FreeSurfer
        FreeSurferSurface = lh.occip.patch.3d.asc
        LocalDomainParent = lh.smoothwm.tlrc.ply
        SurfaceState = occip.patch.3d
        EmbedDimension = 3

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = FreeSurfer
        FreeSurferSurface = lh.occip.patch.flat.asc
        LocalDomainParent = lh.smoothwm.tlrc.ply
        SurfaceState = occip.patch.flat
        EmbedDimension = 2

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = FreeSurfer
        FreeSurferSurface = lh.full.patch.3d.asc
        LocalDomainParent = lh.smoothwm.tlrc.ply
        SurfaceState = full.patch.3d
        EmbedDimension = 3

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = FreeSurfer
        FreeSurferSurface = lh.full.patch.flat.asc
        LocalDomainParent = lh.smoothwm.tlrc.ply
        SurfaceState = full.patch.flat
        EmbedDimension = 2

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = FreeSurfer
        FreeSurferSurface = lh.sphere.asc
        LocalDomainParent = lh.smoothwm.tlrc.ply
        SurfaceState = sphere
        EmbedDimension = 3

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = Ply
        FreeSurferSurface = lh.white.tlrc.ply
        LocalDomainParent = lh.smoothwm.tlrc.ply
        SurfaceState = white
        EmbedDimension = 3

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = FreeSurfer
        FreeSurferSurface = lh.sphere.reg.asc
        LocalDomainParent = lh.smoothwm.tlrc.ply
        SurfaceState = sphere.reg
        EmbedDimension = 3

