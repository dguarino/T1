import numpy
import mozaik
import pylab
from mozaik.visualization.plotting import *
from mozaik.analysis.technical import NeuronAnnotationsToPerNeuronValues
from mozaik.analysis.analysis import *
from mozaik.analysis.vision import *
from mozaik.storage.queries import *
from mozaik.storage.datastore import PickledDataStore
from mozaik.tools.circ_stat import circular_dist
import sys
sys.path.append('/home/do/mozaik/mozaik/mozaik-contrib')
# from Kremkow_plots import *

def perform_analysis_and_visualization(data_store):
    analog_Xon_ids = sorted( param_filter_query(data_store,sheet_name="X_ON").get_segments()[0].get_stored_vm_ids() )
    analog_Xoff_ids = sorted( param_filter_query(data_store,sheet_name="X_OFF").get_segments()[0].get_stored_vm_ids() )
    analog_ids = sorted( param_filter_query(data_store,sheet_name="V1_Exc_L4").get_segments()[0].get_stored_vm_ids() )
    analog_ids_inh = sorted( param_filter_query(data_store,sheet_name="V1_Inh_L4").get_segments()[0].get_stored_vm_ids() )
    # analog_ids = param_filter_query(data_store,sheet_name="V1_Exc_L4").get_segments()[0].get_stored_esyn_ids()
    # analog_ids_inh = param_filter_query(data_store,sheet_name="V1_Inh_L4").get_segments()[0].get_stored_esyn_ids()
    print "analog_Xon_ids: ",analog_Xon_ids
    print "analog_Xoff_ids: ",analog_Xoff_ids
    print "analog_ids: ",analog_ids
    print "analog_ids_inh: ",analog_ids_inh

    # ORIENTATION
    #find neuron with preference close to 0  
    # NeuronAnnotationsToPerNeuronValues(data_store,ParameterSet({})).analyse()
    # l4_exc_or = data_store.get_analysis_result(identifier='PerNeuronValue',value_name = 'LGNAfferentOrientation', sheet_name = 'V1_Exc_L4')
    # l4_exc_phase = data_store.get_analysis_result(identifier='PerNeuronValue',value_name = 'LGNAfferentPhase', sheet_name = 'V1_Exc_L4')
    # l4_exc = analog_ids[numpy.argmin([circular_dist(o,numpy.pi/2,numpy.pi)  for (o,p) in zip(l4_exc_or[0].get_value_by_id(analog_ids),l4_exc_phase[0].get_value_by_id(analog_ids))])]
    # l4_inh_or = data_store.get_analysis_result(identifier='PerNeuronValue',value_name = 'LGNAfferentOrientation', sheet_name = 'V1_Inh_L4')
    # l4_inh_phase = data_store.get_analysis_result(identifier='PerNeuronValue',value_name = 'LGNAfferentPhase', sheet_name = 'V1_Inh_L4')
    # l4_inh = analog_ids_inh[numpy.argmin([circular_dist(o,numpy.pi/2,numpy.pi)  for (o,p) in zip(l4_inh_or[0].get_value_by_id(analog_ids_inh),l4_inh_phase[0].get_value_by_id(analog_ids_inh))])]
    # l4_exc_or_many = numpy.array(l4_exc_or[0].ids)[numpy.nonzero(numpy.array([circular_dist(o,numpy.pi/2,numpy.pi)  for (o,p) in zip(l4_exc_or[0].values,l4_exc_phase[0].values)]) < 0.1)[0]]
    # print "Prefered orientation of plotted exc neurons:"
    # print 'index ' + str(l4_exc)
    # print "Prefered phase of plotted exc neurons:"
    # print l4_exc_phase[0].get_value_by_id(l4_exc)
    # print "Prefered orientation of plotted inh neurons:"
    # print l4_inh_phase[0].get_value_by_id(l4_inh)
    # print 'index ' + str(l4_inh)
    # print "Prefered phase of plotted inh neurons:"
    # print l4_exc_phase[0].get_value_by_id(l4_exc)

    # ---- ANALYSIS ----
    if True: 
        print "\nAnalysis ..."

        ##-------------------------------------
        ## LUMINANCE SENSITIVITY
        # dsv0_Xon = param_filter_query( data_store, st_name='Null', sheet_name='X_ON' )  
        # TrialAveragedFiringRate( dsv0_Xon, ParameterSet({}) ).analyse()
        # dsv0_Xoff = param_filter_query( data_store, st_name='Null', sheet_name='X_OFF' )  
        # TrialAveragedFiringRate( dsv0_Xoff, ParameterSet({}) ).analyse()
        # dsv0_V1e = param_filter_query( data_store, st_name='Null', sheet_name='V1_Exc_L4' )  
        # TrialAveragedFiringRate( dsv0_V1e, ParameterSet({}) ).analyse()
        # dsv0_V1i = param_filter_query( data_store, st_name='Null', sheet_name='V1_Inh_L4' )  
        # TrialAveragedFiringRate( dsv0_V1i, ParameterSet({}) ).analyse()

        ##-------------------------------------
        ## CONTRAST SENSITIVITY, SPATIAL AND TEMPORAL FREQUENCY TUNING, SPARSENESS
        # dsv10 = param_filter_query( data_store, st_name='FullfieldDriftingSinusoidalGrating', sheet_name='X_ON' )  
        # TrialAveragedFiringRate( dsv10, ParameterSet({}) ).analyse()
        # dsv11 = param_filter_query( data_store, st_name='FullfieldDriftingSinusoidalGrating', sheet_name='X_OFF' )  
        # TrialAveragedFiringRate( dsv11, ParameterSet({}) ).analyse()
        # dsv1_V1e = param_filter_query( data_store, st_name='FullfieldDriftingSinusoidalGrating', sheet_name='V1_Exc_L4' )  
        # TrialAveragedFiringRate( dsv1_V1e, ParameterSet({}) ).analyse()
        # dsv1_V1i = param_filter_query( data_store, st_name='FullfieldDriftingSinusoidalGrating', sheet_name='V1_Inh_L4' )  
        # TrialAveragedFiringRate( dsv1_V1i, ParameterSet({}) ).analyse()
        # X ON cell 
        # TrialAveragedSparseness( dsv10, ParameterSet({}) ).analyse() # on responses: Sparseness
        # Analog_MeanSTDAndFanoFactor( dsv10, ParameterSet({}) ).analyse() # on Vm: FanoFactor

        ##-------------------------------------
        ## SIZE TUNING
        dsv10 = param_filter_query( data_store, st_name='DriftingSinusoidalGratingDisk', sheet_name='X_ON' )  
        TrialAveragedFiringRate( dsv10, ParameterSet({}) ).analyse() # on responses
        dsv11 = param_filter_query( data_store, st_name='DriftingSinusoidalGratingDisk', sheet_name='V1_Exc_L4' )  
        TrialAveragedFiringRate( dsv11, ParameterSet({}) ).analyse() # on responses
        dsv12 = param_filter_query( data_store, st_name='FlatDisk', sheet_name='X_ON' )  
        TrialAveragedFiringRate( dsv12, ParameterSet({}) ).analyse() # on responses
        dsv13 = param_filter_query( data_store, st_name='FlatDisk', sheet_name='V1_Exc_L4' )  
        TrialAveragedFiringRate( dsv13, ParameterSet({}) ).analyse() # on responses

        ##-------------------------------------
        ## ORIENTATION TUNING
        # dsv = param_filter_query( data_store, sheet_name='V1_Exc_L4' )
        # ActionPotentialRemoval( dsv, ParameterSet({'window_length' : 10.0}) ).analyse()
        # TrialAveragedFiringRate( param_filter_query( data_store, sheet_name=['V1_Exc_L4','V1_Inh_L4'], st_name="FullfieldDriftingSinusoidalGrating" ), ParameterSet({}) ).analyse()
                
        # dsv = param_filter_query(data_store,st_name='FullfieldDriftingSinusoidalGrating',analysis_algorithm='TrialAveragedFiringRate',sheet_name=['V1_Exc_L4','V1_Inh_L4'])    
        # GaussianTuningCurveFit(dsv,ParameterSet({'parameter_name' : 'orientation'})).analyse()
        # dsv = param_filter_query(data_store,st_name='FullfieldDriftingSinusoidalGrating',sheet_name=['V1_Exc_L4','V1_Inh_L4'])   
        # Analog_F0andF1(dsv,ParameterSet({})).analyse()
    
        # Analog_MeanSTDAndFanoFactor(data_store,ParameterSet({})).analyse()

        # PSTH(param_filter_query(data_store,sheet_name='V1_Exc_L4'),ParameterSet({'bin_length' : 2.0 })).analyse()
        
        # GSTA(param_filter_query(data_store,sheet_name='V1_Exc_L4',st_name='InternalStimulus',direct_stimulation_name='None'),ParameterSet({'neurons' : [l4_exc], 'length' : 250.0 }),tags=['GSTA']).analyse()
        # GSTA(param_filter_query(data_store,sheet_name='V1_Exc_L4',st_name='FullfieldDriftingSinusoidalGrating',st_orientation=[0,numpy.pi/2]),ParameterSet({'neurons' : [l4_exc], 'length' : 250.0 }),tags=['GSTA']).analyse()
        # GSTA(param_filter_query(data_store,sheet_name='V1_Inh_L4',st_name='FullfieldDriftingSinusoidalGrating',st_orientation=[0,numpy.pi/2]),ParameterSet({'neurons' : [l4_inh], 'length' : 250.0 }),tags=['GSTA']).analyse()            
        # GSTA(param_filter_query(data_store,sheet_name='V1_Exc_L4',st_name='NaturalImageWithEyeMovement'),ParameterSet({'neurons' : [l4_exc], 'length' : 250.0 }),tags=['GSTA']).analyse()
        
        # dsv = param_filter_query(data_store,st_name='NaturalImageWithEyeMovement',sheet_name='V1_Exc_L4',analysis_algorithm='ActionPotentialRemoval')
        # TrialVariability(dsv,ParameterSet({'vm': False,  'cond_exc': False, 'cond_inh': False})).analyse()
        # dsv = param_filter_query(data_store,st_name='FullfieldDriftingSinusoidalGrating',sheet_name='V1_Exc_L4',st_contrast=100,analysis_algorithm='ActionPotentialRemoval')            
        # TrialVariability(dsv,ParameterSet({'vm': False,  'cond_exc': False, 'cond_inh': False})).analyse()

        # dsv = param_filter_query(data_store,st_name='FullfieldDriftingSinusoidalGrating',analysis_algorithm='TrialAveragedFiringRate',sheet_name=['V1_Exc_L4','V1_Inh_L4'])  
        # PeriodicTuningCurvePreferenceAndSelectivity_VectorAverage(dsv,ParameterSet({'parameter_name' : 'orientation'})).analyse()
    
        # pnv = param_filter_query(data_store,st_name='InternalStimulus',sheet_name='V1_Exc_L4',analysis_algorithm=['Analog_MeanSTDAndFanoFactor'],value_name='Mean(ECond)',st_direct_stimulation_name='None').get_analysis_result()[0]
        # dsv = param_filter_query(data_store,st_name='FullfieldDriftingSinusoidalGrating',sheet_name='V1_Exc_L4',analysis_algorithm=['Analog_F0andF1'],value_name='F0_Exc_Cond')
        # SubtractPNVfromPNVS(pnv,dsv,ParameterSet({})).analyse()

        # pnv = param_filter_query(data_store,st_name='InternalStimulus',sheet_name='V1_Exc_L4',analysis_algorithm=['Analog_MeanSTDAndFanoFactor'],value_name='Mean(ICond)',st_direct_stimulation_name='None').get_analysis_result()[0]
        # dsv = param_filter_query(data_store,st_name='FullfieldDriftingSinusoidalGrating',sheet_name='V1_Exc_L4',analysis_algorithm=['Analog_F0andF1'],value_name='F0_Inh_Cond')
        # SubtractPNVfromPNVS(pnv,dsv,ParameterSet({})).analyse()

        # pnv = param_filter_query(data_store,st_name='InternalStimulus',sheet_name='V1_Exc_L4',analysis_algorithm=['Analog_MeanSTDAndFanoFactor'],value_name='Mean(VM)',st_direct_stimulation_name='None').get_analysis_result()[0]
        # dsv = param_filter_query(data_store,st_name='FullfieldDriftingSinusoidalGrating',sheet_name='V1_Exc_L4',analysis_algorithm=['Analog_F0andF1'],value_name='F0_Vm')
        # SubtractPNVfromPNVS(pnv,dsv,ParameterSet({})).analyse()
        
        # # ORIENTATION TUNING LGN
        # dsv20 = param_filter_query( data_store, st_name='FullfieldDriftingSinusoidalGrating', sheet_name='X_ON' ) 
        # TrialAveragedFiringRate( dsv20, ParameterSet({}) ).analyse()
        # dsv21 = param_filter_query( data_store, st_name='FullfieldDriftingSinusoidalGrating', sheet_name='X_OFF' ) 
        # TrialAveragedFiringRate( dsv21, ParameterSet({}) ).analyse()

        ##-------------------------------------
        ## CONTOUR-INDUCED CORRELATION
        # dsv30 = param_filter_query( data_store, st_name='FullfieldDriftingSquareGrating', sheet_name='X_ON')
        # TrialAveragedCorrectedCrossCorrelation( dsv30, ParameterSet({'bins':35,'bin_length':5.0,'neurons':analog_Xon_ids,'size':0.1}) ).analyse()
        # dsv31 = param_filter_query( data_store, st_name='FlashingSquares', sheet_name='X_ON')
        # TrialAveragedCorrectedCrossCorrelation( dsv31, ParameterSet({'bins':35,'bin_length':5.0,'neurons':analog_Xon_ids,'size':0.1}) ).analyse()
        # dsv32 = param_filter_query( data_store, st_name='FullfieldDriftingSquareGrating', sheet_name='V1_Exc_L4')
        # TrialAveragedCorrectedCrossCorrelation( dsv32, ParameterSet({'bins':35,'bin_length':5.0,'neurons':analog_ids,'size':0.1}) ).analyse()
        # dsv33 = param_filter_query( data_store, st_name='FlashingSquares', sheet_name='V1_Exc_L4')
        # TrialAveragedCorrectedCrossCorrelation( dsv33, ParameterSet({'bins':35,'bin_length':5.0,'neurons':analog_ids,'size':0.1}) ).analyse()

        ##-------------------------------------
        ## CROSS CORRELATION
        # dsv = param_filter_query(data_store,analysis_algorithm='TrialToTrialCrossCorrelationOfAnalogSignalList')                
        # dsv.print_content(full_ADS=True)


    if True: # ---- PLOTTING ----
        print "\nPlotting ..."
        #----------------------
        # LUMINANCE SENSITIVITY  
        # firing rate against luminance levels              
        # dsv = param_filter_query( data_store, st_name='Null', analysis_algorithm=['TrialAveragedFiringRate'] )
        # PlotTuningCurve(
        #    dsv,
        #    ParameterSet({
        #         'polar': False,
        #         'pool': False,
        #         'centered': False,
        #         'mean': False,
        #         'parameter_name' : 'background_luminance', 
        #         'neurons': list(analog_Xon_ids), 
        #         'sheet_name' : 'X_ON'
        #    }), 
        #    fig_param={'dpi' : 100,'figsize': (30,8)}, 
        #    plot_file_name="FlatLuminanceSensitivity_LGN_On.png"
        # ).plot({
        #    '*.y_lim':(0,30), 
        #    # '*.x_lim':(-10,100), 
        #    '*.fontsize':17
        # })
        # PlotTuningCurve(
        #    dsv,
        #    ParameterSet({
        #         'polar': False,
        #         'pool': False,
        #         'centered': False,
        #         'mean': False,
        #         'parameter_name' : 'background_luminance', 
        #         'neurons': list(analog_Xoff_ids), 
        #         'sheet_name' : 'X_OFF'
        #    }), 
        #    fig_param={'dpi' : 100,'figsize': (30,8)}, 
        #    plot_file_name="FlatLuminanceSensitivity_LGN_Off.png"
        # ).plot({
        #    '*.y_lim':(0,30), 
        #    # '*.x_lim':(-10,100), 
        #    '*.fontsize':17
        # })
        # PlotTuningCurve(
        #    dsv,
        #    ParameterSet({
        #         'polar': False,
        #         'pool': False,
        #         'centered': False,
        #         'mean': False,
        #         'parameter_name' : 'background_luminance', 
        #         'neurons': list(analog_ids), 
        #         'sheet_name' : 'V1_Exc_L4'
        #    }), 
        #    fig_param={'dpi' : 100,'figsize': (30,8)}, 
        #    plot_file_name="FlatLuminanceSensitivity_V1e.png"
        # ).plot({
        #    '*.y_lim':(0,30), 
        #    # '*.x_lim':(-10,100), 
        #    '*.fontsize':17
        # })
        # PlotTuningCurve(
        #    dsv,
        #    ParameterSet({
        #         'polar': False,
        #         'pool': False,
        #         'centered': False,
        #         'mean': False,
        #         'parameter_name' : 'background_luminance', 
        #         'neurons': list(analog_ids_inh), 
        #         'sheet_name' : 'V1_Inh_L4'
        #    }), 
        #    fig_param={'dpi' : 100,'figsize': (30,8)}, 
        #    plot_file_name="FlatLuminanceSensitivity_V1i.png"
        # ).plot({
        #    '*.y_lim':(0,30), 
        #    # '*.x_lim':(-10,100), 
        #    '*.fontsize':17
        # })

        #--------------------
        ## CONTRAST SENSITIVITY
        # dsv = param_filter_query( data_store, st_name='FullfieldDriftingSinusoidalGrating', analysis_algorithm=['TrialAveragedFiringRate'] )
        # dsv.print_content(full_ADS=True)
        # PlotTuningCurve(
        #    dsv,
        #    ParameterSet({
        #         'polar': False,
        #         'pool': False,
        #         'centered': False,
        #         'mean': False,
        #         'parameter_name' : 'contrast', 
        #         'neurons': list(analog_Xon_ids), 
        #         'sheet_name' : 'X_ON'
        #    }), 
        #    fig_param={'dpi' : 100,'figsize': (30,8)}, 
        #    plot_file_name="ContrastSensitivity_LGN_On.png"
        # ).plot({
        #    '*.y_lim':(0,80), 
        #    # '*.x_scale':'log', '*.x_scale_base':10,
        #    '*.fontsize':17
        # })
        # PlotTuningCurve(
        #    dsv,
        #    ParameterSet({
        #         'polar': False,
        #         'pool': False,
        #         'centered': False,
        #         'mean': False,
        #         'parameter_name' : 'contrast', 
        #         'neurons': list(analog_Xoff_ids), 
        #         'sheet_name' : 'X_OFF'
        #    }), 
        #    fig_param={'dpi' : 100,'figsize': (30,8)}, 
        #    plot_file_name="ContrastSensitivity_LGN_Off.png"
        # ).plot({
        #    '*.y_lim':(0,80), 
        #    # '*.x_scale':'log', '*.x_scale_base':10,
        #    '*.fontsize':17
        # })
        # dsv = param_filter_query(data_store,st_name='FullfieldDriftingSinusoidalGrating',analysis_algorithm='TrialAveragedFiringRate',sheet_name='V1_Exc_L4')    
        # dsv.print_content(full_ADS=True)
        # PlotTuningCurve(
        #    dsv,
        #    ParameterSet({
        #         'polar': False,
        #         'pool': False,
        #         'centered': False,
        #         'mean': False,
        #         'parameter_name' : 'contrast', 
        #         'neurons': list(analog_ids), 
        #         'sheet_name' : 'V1_Exc_L4'
        #    }), 
        #    fig_param={'dpi' : 100,'figsize': (30,8)}, 
        #    plot_file_name="ContrastSensitivity_V1e.png"
        # ).plot({
        #    '*.y_lim':(0,80), 
        #    # '*.x_scale':'log', '*.x_scale_base':10,
        #    '*.fontsize':17
        # })
        # dsv = param_filter_query(data_store,st_name='FullfieldDriftingSinusoidalGrating',analysis_algorithm='TrialAveragedFiringRate',sheet_name='V1_Inh_L4')    
        # dsv.print_content(full_ADS=True)
        # PlotTuningCurve(
        #    dsv,
        #    ParameterSet({
        #         'polar': False,
        #         'pool': False,
        #         'centered': False,
        #         'mean': False,
        #         'parameter_name' : 'contrast', 
        #         'neurons': list(analog_ids_inh), 
        #         'sheet_name' : 'V1_Inh_L4'
        #    }), 
        #    fig_param={'dpi' : 100,'figsize': (30,8)}, 
        #    plot_file_name="ContrastSensitivity_V1i.png"
        # ).plot({
        #    '*.y_lim':(0,80), 
        #    # '*.x_scale':'log', '*.x_scale_base':10,
        #    '*.fontsize':17
        # })

        # -----------------
        # SPATIAL FREQUENCY TUNING
        # firing rate against spatial frequencies
        # dsv = param_filter_query( data_store, st_name='FullfieldDriftingSinusoidalGrating', analysis_algorithm=['TrialAveragedFiringRate'] )
        # dsv.print_content(full_ADS=True)
        # PlotTuningCurve(
        #    dsv,
        #    ParameterSet({
        #        'polar': False,
        #        'pool': False,
        #        'centered': False,
        #        'mean': False,
        #        'parameter_name' : 'spatial_frequency', 
        #        'neurons': list(analog_Xon_ids), 
        #        'sheet_name' : 'X_ON'
        #    }), 
        #    fig_param={'dpi' : 50,'figsize': (30,8)}, 
        #    plot_file_name="SpatialFrequencyTuning_LGN_On.png"
        # ).plot({
        #    # '*.y_lim':(0,60), 
        #    #'*.x_scale':'log', '*.x_scale_base':2,
        #    '*.fontsize':17
        # })
        # PlotTuningCurve(
        #    dsv,
        #    ParameterSet({
        #        'polar': False,
        #        'pool': False,
        #        'centered': False,
        #        'mean': False,
        #        'parameter_name' : 'spatial_frequency', 
        #        'neurons': list(analog_Xoff_ids), 
        #        'sheet_name' : 'X_OFF'
        #    }), 
        #    fig_param={'dpi' : 50,'figsize': (30,8)}, 
        #    plot_file_name="SpatialFrequencyTuning_LGN_Off.png"
        # ).plot({
        #    # '*.y_lim':(0,60), 
        #    #'*.x_scale':'log', '*.x_scale_base':2,
        #    '*.fontsize':17
        # })
        # PlotTuningCurve(
        #    dsv,
        #    ParameterSet({
        #        'polar': False,
        #        'pool': False,
        #        'centered': False,
        #        'mean': False,
        #        'parameter_name' : 'spatial_frequency', 
        #        'neurons': list(analog_ids), 
        #        'sheet_name' : 'V1_Exc_L4'
        #    }), 
        #    fig_param={'dpi' : 50,'figsize': (30,8)}, 
        #    plot_file_name="SpatialFrequencyTuning_V1e.png"
        # ).plot({
        #    #'*.y_lim':(0,60), 
        #    #'*.x_scale':'log', '*.x_scale_base':2,
        #    '*.fontsize':17
        # })
        # PlotTuningCurve(
        #    dsv,
        #    ParameterSet({
        #        'polar': False,
        #        'pool': False,
        #        'centered': False,
        #        'mean': False,
        #        'parameter_name' : 'spatial_frequency', 
        #        'neurons': list(analog_ids_inh), 
        #        'sheet_name' : 'V1_Inh_L4'
        #    }), 
        #    fig_param={'dpi' : 50,'figsize': (30,8)}, 
        #    plot_file_name="SpatialFrequencyTuning_V1i.png"
        # ).plot({
        #    # '*.y_lim':(0,60), 
        #    #'*.x_scale':'log', '*.x_scale_base':2,
        #    '*.fontsize':17
        # })

        #-----------------
        # TEMPORAL FREQUENCY TUNING                
        # dsv = param_filter_query( data_store, st_name='FullfieldDriftingSinusoidalGrating', analysis_algorithm=['TrialAveragedFiringRate'] )
        # PlotTuningCurve(
        #    dsv,
        #    ParameterSet({
        #        'polar': False,
        #        'pool': False,
        #        'centered': False,
        #        'mean': False,
        #        'parameter_name' : 'temporal_frequency', 
        #        'neurons': list(analog_Xon_ids), 
        #        'sheet_name' : 'X_ON'
        #   }), 
        #   fig_param={'dpi' : 100,'figsize': (30,8)}, 
        #   plot_file_name="TemporalFrequencyTuning_LGN_On.png"
        # ).plot({
        #     '*.y_lim':(0,60), 
        #     '*.x_scale':'log', '*.x_scale_base':2,
        #     '*.fontsize':27
        # })
        # PlotTuningCurve(
        #    dsv,
        #    ParameterSet({
        #        'polar': False,
        #        'pool': False,
        #        'centered': False,
        #        'mean': False,
        #        'parameter_name' : 'temporal_frequency', 
        #        'neurons': list(analog_Xoff_ids), 
        #        'sheet_name' : 'X_OFF'
        #   }), 
        #   fig_param={'dpi' : 100,'figsize': (30,8)}, 
        #   plot_file_name="TemporalFrequencyTuning_LGN_Off.png"
        # ).plot({
        #     '*.y_lim':(0,60), 
        #     '*.x_scale':'log', '*.x_scale_base':2,
        #     '*.fontsize':27
        # })
        # PlotTuningCurve(
        #    dsv,
        #    ParameterSet({
        #        'polar': False,
        #        'pool': False,
        #        'centered': False,
        #        'mean': False,
        #        'parameter_name' : 'temporal_frequency', 
        #        'neurons': list(analog_ids), 
        #        'sheet_name' : 'V1_Exc_L4'
        #   }), 
        #   fig_param={'dpi' : 100,'figsize': (30,8)}, 
        #   plot_file_name="TemporalFrequencyTuning_V1e.png"
        # ).plot({
        #     '*.y_lim':(0,60), 
        #     '*.x_scale':'log', '*.x_scale_base':2,
        #     '*.fontsize':27
        # })
        # PlotTuningCurve(
        #    dsv,
        #    ParameterSet({
        #        'polar': False,
        #        'pool': False,
        #        'centered': False,
        #        'mean': False,
        #        'parameter_name' : 'temporal_frequency', 
        #        'neurons': list(analog_ids_inh), 
        #        'sheet_name' : 'V1_Inh_L4'
        #   }), 
        #   fig_param={'dpi' : 100,'figsize': (30,8)}, 
        #   plot_file_name="TemporalFrequencyTuning_V1i.png"
        # ).plot({
        #     '*.y_lim':(0,60), 
        #     '*.x_scale':'log', '*.x_scale_base':2,
        #     '*.fontsize':27
        # })

        #------------
        # SIZE TUNING
        # firing rate against sizes
        dsv = param_filter_query( data_store, st_name='DriftingSinusoidalGratingDisk', analysis_algorithm=['TrialAveragedFiringRate'] )
        PlotTuningCurve(
            dsv,
            ParameterSet({
                'polar': False,
                'pool': False,
                'centered': False,
                'mean': False,
                'parameter_name' : 'radius', 
                'neurons': list(analog_Xon_ids), 
                'sheet_name' : 'X_ON'
            }), 
            fig_param={'dpi' : 100,'figsize': (30,8)}, 
            plot_file_name="SizeTuning_Grating_LGN_On.png"
        ).plot({
            '*.y_lim':(0,100), 
            '*.x_scale':'log', '*.x_scale_base':2,
            '*.fontsize':17
        })
        # PlotTuningCurve(
        #     dsv,
        #     ParameterSet({
        #         'polar': False,
        #         'pool': False,
        #         'centered': False,
        #         'mean': False,
        #         'parameter_name' : 'radius', 
        #         'neurons': list(analog_ids), 
        #         'sheet_name' : 'V1_Exc_L4'
        #     }), 
        #     fig_param={'dpi' : 100,'figsize': (30,8)}, 
        #     plot_file_name="SizeTuning_Grating_l4_exc.png"
        # ).plot({
        #     '*.y_lim':(0,100), 
        #     # '*.x_scale':'log', '*.x_scale_base':2,
        #     '*.fontsize':17
        # })
        dsv = param_filter_query( data_store, st_name='FlatDisk', analysis_algorithm=['TrialAveragedFiringRate'] )
        PlotTuningCurve(
           dsv,
           ParameterSet({
                'polar': False,
                'pool': False,
                'centered': False,
                'mean': False,
                'parameter_name' : 'radius', 
                'neurons': list(analog_Xon_ids), 
                'sheet_name' : 'X_ON'
           }), 
            fig_param={'dpi' : 100,'figsize': (30,8)}, 
           plot_file_name="SizeTuning_Disk_LGN_On.png"
        ).plot({
           '*.y_lim':(0,100), 
           '*.x_scale':'log', '*.x_scale_base':2,
           '*.fontsize':17
        })
        # PlotTuningCurve(
        #    dsv,
        #    ParameterSet({
        #         'polar': False,
        #         'pool': False,
        #         'centered': False,
        #         'mean': False,
        #         'parameter_name' : 'radius', 
        #         'neurons': list(analog_ids), 
        #         'sheet_name' : 'V1_Exc_L4'
        #    }), 
        #     fig_param={'dpi' : 100,'figsize': (30,8)}, 
        #    plot_file_name="SizeTuning_Disk_l4_exc.png"
        # ).plot({
        #    '*.y_lim':(0,100), 
        #    '*.x_scale':'log', '*.x_scale_base':2,
        #    '*.fontsize':17
        # })

        #--------------------
        # LIFELONG SPARSENESS
        # # per neuron FanoFactor level
        # dsv = param_filter_query(data_store, analysis_algorithm=['Analog_MeanSTDAndFanoFactor'], sheet_name=['X_ON'], value_name='FanoFactor(VM)')   
        # PerNeuronValuePlot(
        #    dsv,
        #    ParameterSet({'cortical_view':True}),
        #    fig_param={'dpi' : 100,'figsize': (6,6)}, 
        #    plot_file_name="FanoFactor_LGN_On.png"
        # ).plot({
        #    '*.x_axis' : None, 
        #    '*.fontsize':17
        # })
        # # # per neuron Activity Ratio
        # dsv = param_filter_query(data_store, analysis_algorithm=['TrialAveragedSparseness'], sheet_name=['X_ON'], value_name='Sparseness')   
        # PerNeuronValuePlot(
        #     dsv,
        #     ParameterSet({'cortical_view':True}),
        #     fig_param={'dpi' : 100,'figsize': (6,6)}, 
        #     plot_file_name="Sparseness_LGN_On.png"
        # ).plot({
        #     '*.x_axis' : None, 
        #     '*.fontsize':17
        # })

        #-------------------
        # ORIENTATION TUNING
        # dsv = param_filter_query( data_store, st_name='FullfieldDriftingSinusoidalGrating', analysis_algorithm=['TrialAveragedFiringRate'] )
        # PlotTuningCurve( 
        #   dsv, 
        #   ParameterSet({
        #         'polar': False,
        #         'pool': False,
        #        'centered': False,
        #        'mean': False,
        #       'parameter_name':'orientation', 
        #       'neurons':list(analog_Xon_ids), 
        #       'sheet_name':'X_ON'
        #   }), 
        #   fig_param={'dpi' : 100,'figsize': (6,6)}, 
        #   plot_file_name="OrientationTuning_LGN_On.png"
        # ).plot({
        #   '*.y_lim' : (0,100),
        #    '*.fontsize':17
        # })
        # PlotTuningCurve( 
        #   dsv, 
        #   ParameterSet({
        #         'polar': False,
        #         'pool': False,
        #        'centered': False,
        #        'mean': False,
        #       'parameter_name':'orientation', 
        #       'neurons':list(analog_Xoff_ids), 
        #       'sheet_name':'X_OFF'
        #   }), 
        #   fig_param={'dpi' : 100,'figsize': (6,6)}, 
        #   plot_file_name="OrientationTuning_LGN_Off.png"
        # ).plot({
        #   '*.y_lim' : (0,100),
        #    '*.fontsize':17
        # })

        # # V1        
        # dsv = param_filter_query(data_store,st_name=['InternalStimulus'])        
        # OverviewPlot(dsv,ParameterSet({'sheet_name' : 'V1_Exc_L4', 'neuron' : analog_ids[0], 'sheet_activity' : {}}),fig_param={'dpi' : 100,'figsize': (28,12)},plot_file_name='SSExcAnalog.png').plot()
        # OverviewPlot(dsv,ParameterSet({'sheet_name' : 'V1_Inh_L4', 'neuron' : analog_ids_inh[0], 'sheet_activity' : {}}),fig_param={'dpi' : 100,'figsize': (28,12)},plot_file_name='SSInhAnalog.png').plot()    

        # if False:            
        #     TrialToTrialVariabilityComparison(data_store,ParameterSet({}),plot_file_name='TtTVar.png').plot()

        #     dsv = param_filter_query(data_store,st_name='NaturalImageWithEyeMovement')            
        #     KremkowOverviewFigure(dsv,ParameterSet({'neuron' : l4_exc,'sheet_name' : 'V1_Exc_L4'}),fig_param={'dpi' : 100,'figsize': (19,12)},plot_file_name='NMOverview.png').plot()            

        # if True:
        #     dsv = param_filter_query(data_store,st_name='FullfieldDriftingSinusoidalGrating',st_contrast=100)    
        #     OverviewPlot(dsv,ParameterSet({'sheet_name' : 'V1_Exc_L4', 'neuron' : l4_exc, 'sheet_activity' : {}}),fig_param={'dpi' : 100,'figsize': (19,12)},plot_file_name="Exc2.png").plot({'Vm_plot.y_lim' : (-67,-56),'Conductance_plot.y_lim' : (0,35.0)})
        #     OverviewPlot(dsv,ParameterSet({'sheet_name' : 'V1_Exc_L4', 'neuron' : analog_ids[0], 'sheet_activity' : {}}),fig_param={'dpi' : 100,'figsize': (19,12)},plot_file_name="Exc3.png").plot({'Vm_plot.y_lim' : (-67,-56),'Conductance_plot.y_lim' : (0,35.0)})
        #     OverviewPlot(dsv,ParameterSet({'sheet_name' : 'V1_Exc_L4', 'neuron' : analog_ids[1], 'sheet_activity' : {}}),fig_param={'dpi' : 100,'figsize': (19,12)},plot_file_name="Exc4.png").plot({'Vm_plot.y_lim' : (-67,-56),'Conductance_plot.y_lim' : (0,35.0)})
        #     OverviewPlot(dsv,ParameterSet({'sheet_name' : 'V1_Exc_L4', 'neuron' : analog_ids[2], 'sheet_activity' : {}}),fig_param={'dpi' : 100,'figsize': (19,12)},plot_file_name="Exc5.png").plot({'Vm_plot.y_lim' : (-67,-56),'Conductance_plot.y_lim' : (0,35.0)})
        #     OverviewPlot(dsv,ParameterSet({'sheet_name' : 'V1_Exc_L4', 'neuron' : analog_ids[3], 'sheet_activity' : {}}),fig_param={'dpi' : 100,'figsize': (19,12)},plot_file_name="Exc6.png").plot({'Vm_plot.y_lim' : (-67,-56),'Conductance_plot.y_lim' : (0,35.0)})
        #     OverviewPlot(dsv,ParameterSet({'sheet_name' : 'V1_Exc_L4', 'neuron' : analog_ids[4], 'sheet_activity' : {}}),fig_param={'dpi' : 100,'figsize': (19,12)},plot_file_name="Exc7.png").plot({'Vm_plot.y_lim' : (-67,-56),'Conductance_plot.y_lim' : (0,35.0)})
        #     OverviewPlot(dsv,ParameterSet({'sheet_name' : 'V1_Exc_L4', 'neuron' : analog_ids[5], 'sheet_activity' : {}}),fig_param={'dpi' : 100,'figsize': (19,12)},plot_file_name="Exc8.png").plot({'Vm_plot.y_lim' : (-67,-56),'Conductance_plot.y_lim' : (0,35.0)})
        #     OverviewPlot(dsv,ParameterSet({'sheet_name' : 'V1_Exc_L4', 'neuron' : analog_ids[6], 'sheet_activity' : {}}),fig_param={'dpi' : 100,'figsize': (19,12)},plot_file_name="Exc9.png").plot({'Vm_plot.y_lim' : (-67,-56),'Conductance_plot.y_lim' : (0,35.0)})
        #     OverviewPlot(dsv,ParameterSet({'sheet_name' : 'V1_Exc_L4', 'neuron' : analog_ids[7], 'sheet_activity' : {}}),fig_param={'dpi' : 100,'figsize': (19,12)},plot_file_name="Exc10.png").plot({'Vm_plot.y_lim' : (-67,-56),'Conductance_plot.y_lim' : (0,35.0)})

            
        #     OverviewPlot(dsv,ParameterSet({'sheet_name' : 'V1_Inh_L4', 'neuron' : l4_inh, 'sheet_activity' : {}}),fig_param={'dpi' : 100,'figsize': (14,12)},plot_file_name="Inh.png").plot({'Vm_plot.y_lim' : (-67,-56),'Conductance_plot.y_lim' : (0,35.0)})
        #     OverviewPlot(dsv,ParameterSet({'sheet_name' : 'X_ON', 'neuron' : sorted(param_filter_query(data_store,sheet_name="X_ON").get_segments()[0].get_stored_esyn_ids())[0], 'sheet_activity' : {}}),fig_param={'dpi' : 100,'figsize': (14,12)},plot_file_name="LGN0On.png").plot()
        #     OverviewPlot(dsv,ParameterSet({'sheet_name' : 'X_OFF', 'neuron' : sorted(param_filter_query(data_store,sheet_name="X_OFF").get_segments()[0].get_stored_esyn_ids())[0], 'sheet_activity' : {}}),fig_param={'dpi' : 100,'figsize': (14,12)},plot_file_name="LGN0Off.png").plot()
        #     OverviewPlot(dsv,ParameterSet({'sheet_name' : 'X_ON', 'neuron' : sorted(param_filter_query(data_store,sheet_name="X_ON").get_segments()[0].get_stored_esyn_ids())[1], 'sheet_activity' : {}}),fig_param={'dpi' : 100,'figsize': (14,12)},plot_file_name="LGN1On.png").plot()
        #     OverviewPlot(dsv,ParameterSet({'sheet_name' : 'X_OFF', 'neuron' : sorted(param_filter_query(data_store,sheet_name="X_OFF").get_segments()[0].get_stored_esyn_ids())[1], 'sheet_activity' : {}}),fig_param={'dpi' : 100,'figsize': (14,12)},plot_file_name="LGN1Off.png").plot()
        
        # # tuning curves
        # dsv = param_filter_query(data_store,st_name='FullfieldDriftingSinusoidalGrating',analysis_algorithm=['TrialAveragedFiringRate','Analog_F0andF1'])    
        # PlotTuningCurve(dsv,ParameterSet({'parameter_name' : 'orientation', 'neurons': list(analog_ids), 'sheet_name' : 'V1_Exc_L4','centered'  : True,'mean' : False,'polar' : False, 'pool' : False}),fig_param={'dpi' : 100,'figsize': (25,12)},plot_file_name="TCExc.png").plot({'TuningCurve F0_Inh_Cond.y_lim' : (0,180) , 'TuningCurve F0_Exc_Cond.y_lim' : (0,80)})
        # PlotTuningCurve(dsv,ParameterSet({'parameter_name' : 'orientation', 'neurons': list(analog_ids_inh), 'sheet_name' : 'V1_Inh_L4','centered'  : True,'mean' : False,'polar' : False, 'pool' : False}),fig_param={'dpi' : 100,'figsize': (25,12)},plot_file_name="TCInh.png").plot({'TuningCurve F0_Inh_Cond.y_lim' : (0,180) , 'TuningCurve F0_Exc_Cond.y_lim' : (0,80)})
        
        # dsv = param_filter_query(data_store,st_name='FullfieldDriftingSinusoidalGrating',analysis_algorithm=['Analog_MeanSTDAndFanoFactor'])    
        # PlotTuningCurve(dsv,ParameterSet({'parameter_name' : 'orientation', 'neurons': list(analog_ids), 'sheet_name' : 'V1_Exc_L4','centered'  : True,'mean' : False,'polar' : False, 'pool' : False}),fig_param={'dpi' : 100,'figsize': (25,12)},plot_file_name="TCExcA.png").plot()
        # PlotTuningCurve(dsv,ParameterSet({'parameter_name' : 'orientation', 'neurons': list(analog_ids_inh), 'sheet_name' : 'V1_Inh_L4','centered'  : True,'mean' : False,'polar' : False, 'pool' : False}),fig_param={'dpi' : 100,'figsize': (25,12)},plot_file_name="TCInhA.png").plot()

        #-----------
        ## CONTOUR COMPLETION
        # ## Square Grating
        # dsv = param_filter_query( data_store, st_name='FullfieldDriftingSquareGrating', analysis_algorithm=['TrialAveragedCorrectedCrossCorrelation'] )
        # PerNeuronPairAnalogSignalListPlot(
        #     dsv,
        #     ParameterSet({
        #         'sheet_name' : 'X_ON', 
        #     }),
        #     fig_param={'dpi' : 100,'figsize': (14,14)}, 
        #     plot_file_name='SquareGrating_XCorr_LGN_On.png'
        # ).plot({
        #     '*.y_lim':(-30,30), 
        #     '*.fontsize':17
        # })
        # PerNeuronPairAnalogSignalListPlot(
        #     dsv,
        #     ParameterSet({
        #         'sheet_name' : 'V1_Exc_L4', 
        #     }),
        #     fig_param={'dpi' : 100,'figsize': (14,14)}, 
        #     plot_file_name='SquareGrating_XCorr_V1e.png'
        # ).plot({
        #     '*.y_lim':(-30,30), 
        #     '*.fontsize':17
        # })
        # ## Flashing squares
        # dsv = param_filter_query( data_store, st_name='FlashingSquares', analysis_algorithm=['TrialAveragedCorrectedCrossCorrelation'] )
        # PerNeuronPairAnalogSignalListPlot(
        #     dsv,
        #     ParameterSet({
        #         'sheet_name' : 'X_ON', 
        #     }),
        #     fig_param={'dpi' : 100,'figsize': (14,14)}, 
        #     plot_file_name='FlashingSquare_XCorr_LGN_On.png'
        # ).plot({
        #     '*.y_lim':(-30,30), 
        #     '*.fontsize':17
        # })
        # PerNeuronPairAnalogSignalListPlot(
        #     dsv,
        #     ParameterSet({
        #         'sheet_name' : 'V1_Exc_L4', 
        #     }),
        #     fig_param={'dpi' : 100,'figsize': (14,14)}, 
        #     plot_file_name='FlashingSquare_XCorr_V1e.png'
        # ).plot({
        #     '*.y_lim':(-30,30), 
        #     '*.fontsize':17
        # })


        import pylab
        # pylab.show()






