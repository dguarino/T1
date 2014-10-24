#!/usr/local/bin/ipython -i 
from mozaik.experiments import *
from mozaik.experiments.vision import *
from mozaik.sheets.population_selector import RCRandomPercentage
from parameters import ParameterSet
    
def create_experiments(model):
  return [

      # SPONTANEOUS ACTIVITY (darkness)
      # as in LevickWilliams1964, WebbTinsleyBarracloughEastonParkerDerrington2002, (TODO: TsumotoCreutzfeldtLegendy1978)
      # NoStimulation( model, duration=147*7),

      # LUMINANCE SENSITIVITY
      # as in PapaioannouWhite1972
      # MeasureFlatLuminanceSensitivity(
      #     model, 
      #     luminances=[0.01, 0.1, 1.0, 10.0, 20.0, 100.0],
      #     step_duration=147*7,
      #     num_trials=14
      # ),

      # CONTRAST SENSITIVITY
      # as in DerringtonLennie1984, HeggelundKarlsenFlugsrudNordtug1989, SaulHumphrey1990, BoninManteCarandini2005
      # MeasureContrastSensitivity(
      #     model, 
      #     size=2.0,
      #     orientation=numpy.pi/2, 
      #     spatial_frequency=0.15, 
      #     temporal_frequency=8.0,
      #     grating_duration=147*7,
      #     contrasts=[0,10,25,40,75,100],
      #     num_trials=14
      # ),

      # SPATIAL AND TEMPORAL FREQUENCY TUNING (with different contrasts)
      # Spatial: as in SolomonWhiteMartin2002, SceniakChatterjeeCallaway2006
      # Temporal: as in SaulHumphrey1990, AlittoUsrey2004
      # MeasureFrequencySensitivity(
      #     model, 
      #     orientation=numpy.pi/2, 
      #     contrasts=[100], #[50], #
      #     spatial_frequencies=[0.01, 0.1, 0.16, 0.24, 0.64, 0.8, 1.0, 1.8], #[0.15], [0.01, 0.1, 0.24, 0.64, 0.8, 1.0, 1.8], #[0.25], #
      #     temporal_frequencies=[6.0], #[0.12, 0.5, 1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0], #[6.0],
      #     grating_duration=147*7,
      #     frame_duration=7,
      #     num_trials=14
      # ),

      # SIZE TUNING
      # as in ClelandLeeVidyasagar1983, BoninManteCarandini2005
      MeasureSizeTuning(
          model, 
          num_sizes=5, 
          max_size=16.0, 
          orientation=numpy.pi/2, 
          spatial_frequency=0.5, #0.15, 
          temporal_frequency=4.0, #8.0,
          grating_duration=147*7,
          contrasts=[100], #40,100  to look for contrast-dependent RF expansion
          num_trials=5,
          log_spacing=True,
          with_flat=True #use also flat luminance discs
      ),
      
      # LIFELONG SPARSENESS
      # as in RathbunWarlandUsrey2010, AndolinaJonesWangSillito2007
      # stimulation as Size Tuning
      
      # ORIENTATION TUNING (GRATINGS)
      # as in DanielsNormanPettigrew1977, VidyasagarUrbas1982
      # MeasureOrientationTuningFullfield(
      #     model,
      #     num_orientations=2, #8,
      #     spatial_frequency=0.3,
      #     temporal_frequency=3.0, #6.0,
      #     grating_duration=147*7,
      #     contrasts=[20,50,100],
      #     num_trials=14
      # ),

      # CONTOUR COMPLETION
      # as in SillitoJonesGersteinWest1994, SillitoCudeiroMurphy1993
      # By default, for this experiment only, the visual space ('size' parameter in the SpatioTemporalFilterRetinaLGN_default file)
      # is reduced to a flat line in order to have an horizontal distribution of neurons.
      # A separation distance is established and the experimental protocol finds the closest neurons to the distance specified.
      # MeasureFeatureInducedCorrelation(
      #     model, 
      #     contrast=70, 
      #     spatial_frequencies=[0.25],
      #     separation=6,
      #     temporal_frequency=2.0,
      #     exp_duration=147*7,
      #     frame_duration=7,
      #     num_trials=10,
      # ),

      # ------------------------------------------
      # IMAGES WITH EYEMOVEMENT
      #MeasureNaturalImagesWithEyeMovement(
      #  model,
      #  stimulus_duration=147*7 *3,
      #  num_trials=5
      #),

      # GRATINGS WITH EYEMOVEMENT
      # MeasureDriftingSineGratingWithEyeMovement(
      #   model, 
      #   spatial_frequency=0.8,
      #   temporal_frequency=2,
      #   stimulus_duration=147*7,
      #   num_trials=10,
      #   contrast=100
      # ),

  ]

