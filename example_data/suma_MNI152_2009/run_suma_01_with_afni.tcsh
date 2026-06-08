#!/bin/tcsh

# This is an example script for driving AFNI+SUMA and having them talk

set suma_spec = std.141.*_both.spec
set all_sv    = ( *SurfVol*{nii,HEAD}* )
set dset_sv   = ${all_sv[1]}

if ( $status || "${?suma_spec}" == "0" ) then
    echo "** Some badness with finding files"
    exit 1
endif

# --------------------- preliminary settings -----------------------

# you can set other env vars if you want
setenv AFNI_ENVIRON_WARNINGS       NO
setenv SUMA_DriveSumaMaxCloseWait   6
setenv SUMA_DriveSumaMaxWait        6

set portnum = 0

# ------------------------- open the GUIs --------------------------

afni -npb ${portnum} -niml  &

sleep 2

suma                                                    \
    -onestate                                           \
    -npb   ${portnum}                                   \
    -spec  ${suma_spec}                                 \
    -sv    ${dset_sv} &

sleep 2

DriveSuma                                               \
    -npb ${portnum}                                     \
    -com viewer_cont -key 't' -key '.' 

# ------------------------- Finish up ---------------------------

if ( $status ) then
    echo "** Some badness with driving SUMA"
    exit 1
endif

echo ""
echo "++ AFNI+SUMA should be up and talking now..."
echo ""

