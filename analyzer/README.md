How to use the LHE analyzer
======================

  cmsrel CMSSW_7_1_14

  cd CMSSW_7_1_14/src/

  cmsenv

  git cms-addpkg GeneratorInterface/LHEInterface

  git cms-merge-topic syuvivida:7114_diboson_lhereader

  scramv1 b

 3. To run,

cmsRun GeneratorInterface/LHEInterface/test/dumpLHE_cfg.py inputFiles="file:xxx.lhe" outputFile="test.root" maxEvents=-1
