# CoVar Readers Digest 

This repo records the CoVar's Reader Digest, a monthly publication recording
papers/results/developments in the literature worth knowing about.  All are
welcomed --- and encouraged! --- to contribute.  

To begin, clone the repo:

```
git clone git@cvr-git.covar.local:common/readers-digest.git
```

Once the repo is cloned, switch over to the active branch.  This will 
be in the form `XXXX_YY` where `XXXX` is the year and `YY` is the
month corresponding to the next Reader's Digest.  Almost always, this
will be the calendar month after the current month.  For instance,
if it is May of 2024 then the active branch of the Reader's Digest will 
be `2024_06`.  Once on the active branch, open the `.rst` file corresponding
to that branch, which will always reside in `readers-digest/docs/issues/`.  
For May of 2024, this would be `2024-06.rst`.  

Inside the `.rst` file, there will be a number of sections to add an
entry.  Find the section best describing the work-to-be-entered, 
or create a new one if an existing one will not suffice. The format is

```
Section Name
------------
```

To describe the work-to-be-entered, it suffices to have a name,
a URL linking to an online version of the work, and a short 
description of the work that is between one and several sentences
in length.  Entries should be of the form:

```
`name of work <url>`_
    Description of work.
```

Please do not merge branches or edit/delte existing entries unless
you have permission to do so.