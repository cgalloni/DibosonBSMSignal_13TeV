import FWCore.ParameterSet.Config as cms

# link to cards:
# https://github.com/cms-sw/genproductions/tree/b5f5fff5a3e2d0c3b4c7583333677dec6de182fa/bin/MadGraph5_aMCatNLO/cards/production/13TeV/exo_diboson/Spin-2/RSGraviton_ZZ_ZlepZhad/RSGraviton_ZZ_ZlepZhad_narrow_M1600


externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.2.2/exo_diboson/Spin-2/RSGraviton_ZZ_ZlepZhad/narrow/v1/RSGraviton_ZZ_ZlepZhad_narrow_M1600_tarball.tar.xz'),
    nEvents = cms.untracked.uint32(5000),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)
