# -*- coding: utf-8 -*-
"""
This is implementation of a full recursive model of thalamo-cortical connectvity
"""
import sys
from pyNN import nest
import mozaik
from mozaik.controller import run_workflow, setup_logging
from model import ThalamoCorticalModel
from experiments import create_experiments
from mozaik.storage.datastore import Hdf5DataStore,PickledDataStore
from analysis_and_visualization import perform_analysis_and_visualization
from parameters import ParameterSet


try:
    from mpi4py import MPI
except ImportError:
    MPI = None
if MPI:
    mpi_comm = MPI.COMM_WORLD
MPI_ROOT = 0

logger = mozaik.getMozaikLogger()

if True:
    data_store,model = run_workflow('T1',ThalamoCorticalModel,create_experiments)
    model.connectors['V1L4ExcL4ExcConnection'].store_connections(data_store)    
    model.connectors['V1L4ExcL4InhConnection'].store_connections(data_store)    
    model.connectors['V1L4InhL4ExcConnection'].store_connections(data_store)    
    model.connectors['V1L4InhL4InhConnection'].store_connections(data_store)    
    model.connectors['V1AffConnectionOn'].store_connections(data_store)    
    model.connectors['V1AffConnectionOff'].store_connections(data_store)    
    model.connectors['V1AffInhConnectionOn'].store_connections(data_store)    
    model.connectors['V1AffInhConnectionOff'].store_connections(data_store)    
    model.connectors['V1Exc_LGN_ON_ExcConnection'].store_connections(data_store)    
    model.connectors['V1Exc_LGN_OFF_ExcConnection'].store_connections(data_store)    
    data_store.save()
    
else: 
    setup_logging()
    data_store = PickledDataStore(load=True,parameters=ParameterSet({'root_directory':'T1_data_____', 'store_stimuli' : False}),replace=True)
    logger.info('Loaded data store')
    data_store.save()

if mpi_comm.rank == MPI_ROOT:
    perform_analysis_and_visualization(data_store)
