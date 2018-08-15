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
        StateDef = white
        StateDef = rh_inflated
        StateDef = rh_occip.patch.3d
        StateDef = rh_occip.patch.flat
        StateDef = rh_full.patch.3d
        StateDef = rh_full.patch.flat
        StateDef = rh_sphere
        StateDef = rh_sphere.reg
        StateDef = lh_inflated
        StateDef = lh_occip.patch.3d
        StateDef = lh_occip.patch.flat
        StateDef = lh_full.patch.3d
        StateDef = lh_full.patch.flat
        StateDef = lh_sphere
        StateDef = lh_sphere.reg

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
        SurfaceState = lh_inflated
        EmbedDimension = 3

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = FreeSurfer
        FreeSurferSurface = lh.occip.patch.3d.asc
        LocalDomainParent = lh.smoothwm.tlrc.ply
        SurfaceState = lh_occip.patch.3d
        EmbedDimension = 3

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = FreeSurfer
        FreeSurferSurface = lh.occip.patch.flat.asc
        LocalDomainParent = lh.smoothwm.tlrc.ply
        SurfaceState = lh_occip.patch.flat
        EmbedDimension = 2

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = FreeSurfer
        FreeSurferSurface = lh.full.patch.3d.asc
        LocalDomainParent = lh.smoothwm.tlrc.ply
        SurfaceState = lh_full.patch.3d
        EmbedDimension = 3

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = FreeSurfer
        FreeSurferSurface = lh.full.patch.flat.asc
        LocalDomainParent = lh.smoothwm.tlrc.ply
        SurfaceState = lh_full.patch.flat
        EmbedDimension = 2

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = FreeSurfer
        FreeSurferSurface = lh.sphere.asc
        LocalDomainParent = lh.smoothwm.tlrc.ply
        SurfaceState = lh_sphere
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
        SurfaceState = lh_sphere.reg
        EmbedDimension = 3

#the right side of things
NewSurface
        SurfaceFormat = ASCII
        SurfaceType = Ply
        FreeSurferSurface = rh.smoothwm.tlrc.ply
        LocalDomainParent = SAME
        SurfaceState = smoothwm
        EmbedDimension = 3

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = Ply
        FreeSurferSurface = rh.pial.tlrc.ply
        LocalDomainParent = rh.smoothwm.tlrc.ply
        SurfaceState = pial
        EmbedDimension = 3

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = FreeSurfer
        FreeSurferSurface = rh.inflated.asc
        LocalDomainParent = rh.smoothwm.tlrc.ply
        SurfaceState = rh_inflated
        EmbedDimension = 3

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = FreeSurfer
        FreeSurferSurface = rh.occip.patch.3d.asc
        LocalDomainParent = rh.smoothwm.tlrc.ply
        SurfaceState = rh_occip.patch.3d
        EmbedDimension = 3

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = FreeSurfer
        FreeSurferSurface = rh.occip.patch.flat.asc
        LocalDomainParent = rh.smoothwm.tlrc.ply
        SurfaceState = rh_occip.patch.flat
        EmbedDimension = 2

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = FreeSurfer
        FreeSurferSurface = rh.full.patch.3d.asc
        LocalDomainParent = rh.smoothwm.tlrc.ply
        SurfaceState = rh_full.patch.3d
        EmbedDimension = 3

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = FreeSurfer
        FreeSurferSurface = rh.full.patch.flat.asc
        LocalDomainParent = rh.smoothwm.tlrc.ply
        SurfaceState = rh_full.patch.flat
        EmbedDimension = 2


NewSurface
        SurfaceFormat = ASCII
        SurfaceType = FreeSurfer
        FreeSurferSurface = rh.sphere.asc
        LocalDomainParent = rh.smoothwm.tlrc.ply
        SurfaceState = rh_sphere
        EmbedDimension = 3

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = Ply
        FreeSurferSurface = rh.white.tlrc.ply
        LocalDomainParent = rh.smoothwm.tlrc.ply
        SurfaceState = white
        EmbedDimension = 3

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = FreeSurfer
        FreeSurferSurface = rh.sphere.reg.asc
        LocalDomainParent = rh.smoothwm.tlrc.ply
        SurfaceState = rh_sphere.reg
        EmbedDimension = 3

