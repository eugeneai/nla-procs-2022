Dear LLNCS user,

The files in this directory belong to the LaTeX2e package for
Lecture Notes in Computer Science (LNCS) of Springer-Verlag.

It consists of the following files:

  readme.txt         this file

  history.txt        the version history of the package

  llncs.cls          the LaTeX2e document class

  llncs.dem          the sample input file

  llncs.doc          the documentation of the class (LaTeX source)
  llncsdoc.pdf       the documentation of the class (PDF version)
  llncsdoc.sty       the modification of the class for the documentation
  llncs.ind          an external (faked) author index file
  subjidx.ind        subject index demo from the Springer book package
  llncs.dvi          the resulting DVI file (remember to use binary transfer!)

  sprmindx.sty       supplementary style file for MakeIndex
                     (usage: makeindex -s sprmindx.sty <yourfile.idx>)

  splncs.bst         old BibTeX style for use with llncs.cls

  splncs_srt.bst     ditto with alphabetic sorting

  splncs03.bst       current LNCS BibTeX style with alphabetic sorting

  aliascnt.sty       part of the Oberdiek bundle; allows more control over
                     the counters associated to any numbered item
  remreset.sty       by David Carlisle

NLA'2018 organizing committee added the following files:

  nla.sty            Correcting style file, adapting llncs.cls to NLA'2018
                     proceedings layout.

  template_eng-1.tex The paper template and instruction for papers in English.

  template_rus-1.tex The paper template and instruction for papers in Russian.

  my-paper-pics      An empty subfolder for pictures.

  Makefile           Makefile for unix users facilitating paper compilation.
                     Usage:  make
                     Add target 'compile' to force the compilation, i.e.,
                     make compile

The llncs class adaptation project site is https://github.com/eugeneai/nla-style.
The NLA'2018 conference site is http://nla.icc.ru/.  We will soon publish there
an instruction on the usage overleaf.com service for the paper preparation.
