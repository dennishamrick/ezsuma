# delimits comments

# Creation information:
#     user    : taylorpa3
#     date    : Tue Aug  9 13:48:01 EDT 2022
#     machine : cn4330
#     pwd     : /lscratch/45374765/MNI152_2009/SUMA
#     command : @SUMA_Make_Spec_FS -fs_setup -NIFTI -sid MNI152_2009 -fspath /lscratch/45374765/MNI152_2009

# define the group
        Group = MNI152_2009

# define various States
        StateDef = smoothwm
        StateDef = pial
        StateDef = inflated
        StateDef = occip.patch.3d
        StateDef = occip.patch.flat
        StateDef = occip.flat.patch.3d
        StateDef = fusiform.patch.flat
        StateDef = full.patch.3d
        StateDef = full.patch.flat
        StateDef = full.flat.patch.3d
        StateDef = full.flat
        StateDef = flat.patch
        StateDef = sphere
        StateDef = white
        StateDef = sphere.reg
        StateDef = rh.sphere.reg
        StateDef = lh.sphere.reg
        StateDef = pial-outer-smoothed
        StateDef = inf_200

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = rh.smoothwm.gii
        LocalDomainParent = SAME
        SurfaceState = smoothwm
        EmbedDimension = 3
        Anatomical = Y
        LabelDset = rh.aparc.a2009s.annot.niml.dset

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = rh.pial.gii
        LocalDomainParent = rh.smoothwm.gii
        SurfaceState = pial
        EmbedDimension = 3
        Anatomical = Y

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = rh.inflated.gii
        LocalDomainParent = rh.smoothwm.gii
        SurfaceState = inflated
        EmbedDimension = 3
        Anatomical = N

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = rh.sphere.gii
        LocalDomainParent = rh.smoothwm.gii
        SurfaceState = sphere
        EmbedDimension = 3
        Anatomical = N

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = rh.white.gii
        LocalDomainParent = rh.smoothwm.gii
        SurfaceState = white
        EmbedDimension = 3
        Anatomical = Y

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = rh.sphere.reg.gii
        LocalDomainParent = rh.smoothwm.gii
        SurfaceState = sphere.reg
        EmbedDimension = 3
        Anatomical = N

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = GIFTI
        SurfaceName = rh.inf_200.gii
        LocalDomainParent = rh.smoothwm.gii
        SurfaceState = inf_200
        EmbedDimension = 3
        Anatomical = N

