#!/usr/bin/env python
'''
@author Luke Campbell <LCampbell@ASAScience.com>
@file extern/parameter-definitions/parameter_definitions/science/standard.py
@date Tue Oct 23 16:12:58 EDT 2012
@brief Plugin for loading the standard set of parameter definitions
'''

def load():
    from coverage_model.parameter import ParameterContext
    from coverage_model.parameter_types import QuantityType, ArrayType, RecordType
    from coverage_model.basic_types import AxisTypeEnum
    import numpy as np
    contexts = []

    cond_ctxt = ParameterContext('conductivity', param_type=QuantityType(value_encoding=np.float32))
    cond_ctxt.uom = 'unknown'
    cond_ctxt.fill_value = 0e0
    contexts.append(cond_ctxt)

    pres_ctxt = ParameterContext('pressure', param_type=QuantityType(value_encoding=np.float32))
    pres_ctxt.uom = 'Pascal'
    pres_ctxt.fill_value = 0x0
    contexts.append(pres_ctxt)

    sal_ctxt = ParameterContext('salinity', param_type=QuantityType(value_encoding=np.float32))
    sal_ctxt.uom = 'PSU'
    sal_ctxt.fill_value = 0x0
    contexts.append(sal_ctxt)

    den_ctxt = ParameterContext('density', param_type=QuantityType(value_encoding=np.float32))
    den_ctxt.uom = 'kg/m3'
    den_ctxt.fill_value = 0x0
    contexts.append(den_ctxt)

    temp_ctxt = ParameterContext('temp', param_type=QuantityType(value_encoding=np.float32))
    temp_ctxt.uom = 'degree_Celsius'
    temp_ctxt.fill_value = 0e0
    contexts.append(temp_ctxt)

    t_ctxt = ParameterContext('time', param_type=QuantityType(value_encoding=np.int64))
    t_ctxt.uom = 'seconds since 1970-01-01'
    t_ctxt.fill_value = 0x0
    contexts.append(t_ctxt)

    lat_ctxt = ParameterContext('lat', param_type=QuantityType(value_encoding=np.float32))
    lat_ctxt.reference_frame = AxisTypeEnum.LAT
    lat_ctxt.uom = 'degree_north'
    lat_ctxt.fill_value = 0e0
    contexts.append(lat_ctxt)

    lon_ctxt = ParameterContext('lon', param_type=QuantityType(value_encoding=np.float32))
    lon_ctxt.reference_frame = AxisTypeEnum.LON
    lon_ctxt.uom = 'degree_east'
    lon_ctxt.fill_value = 0e0
    contexts.append(lon_ctxt)

    raw_ctxt = ParameterContext('raw', param_type=ArrayType())
    raw_ctxt.description = 'raw binary string values'
    raw_ctxt.uom = 'utf-8 byte string'
    raw_ctxt.fill_value = 0x0
    contexts.append(raw_ctxt)

    port_ts_ctxt = ParameterContext(name='port_timestamp', param_type=QuantityType(value_encoding=np.float64))
    port_ts_ctxt._derived_from_name = 'time'
    port_ts_ctxt.uom = 'seconds'
    port_ts_ctxt.fill_value = -1
    contexts.append(port_ts_ctxt)

    driver_ts_ctxt = ParameterContext(name='driver_timestamp', param_type=QuantityType(value_encoding=np.float64))
    driver_ts_ctxt._derived_from_name = 'time'
    driver_ts_ctxt.uom = 'seconds'
    driver_ts_ctxt.fill_value = -1
    contexts.append(driver_ts_ctxt)

    internal_ts_ctxt = ParameterContext(name='internal_timestamp', param_type=QuantityType(value_encoding=np.float64))
    internal_ts_ctxt._derived_from_name = 'time'
    internal_ts_ctxt.uom = 'seconds'
    internal_ts_ctxt.fill_value = -1
    contexts.append(internal_ts_ctxt)

    timer_num_ctxt = ParameterContext(name='timer', param_type=QuantityType(value_encoding=np.float64))
    timer_num_ctxt.fill_value = -1
    contexts.append(timer_num_ctxt)

    serial_num_ctxt = ParameterContext(name='serial_num', param_type=QuantityType(value_encoding=np.int32))
    serial_num_ctxt.fill_value = -1
    contexts.append(serial_num_ctxt)

    count_ctxt = ParameterContext(name='counts', param_type=QuantityType(value_encoding=np.uint64))
    count_ctxt.fill_value = -1
    contexts.append(count_ctxt)

    checksum_ctxt = ParameterContext(name='checksum', param_type=QuantityType(value_encoding=np.int32))
    checksum_ctxt.fill_value = -1
    contexts.append(checksum_ctxt)

    pref_ts_ctxt = ParameterContext(name='preferred_timestamp', param_type=ArrayType())
    pref_ts_ctxt.description = 'name of preferred timestamp'
    pref_ts_ctxt.fill_value = None
    contexts.append(pref_ts_ctxt)

    # TODO: This should probably be of type CategoryType when implemented
    qual_flag_ctxt = ParameterContext(name='quality_flag', param_type=ArrayType())
    qual_flag_ctxt.description = 'flag indicating quality'
    qual_flag_ctxt.fill_value = None
    contexts.append(qual_flag_ctxt)

    viz_ts_ctxt = ParameterContext(name='viz_timestamp', param_type=QuantityType(value_encoding=np.float64))
    viz_ts_ctxt._derived_from_name = 'time'
    viz_ts_ctxt.uom = 'seconds'
    viz_ts_ctxt.fill_value = -1
    contexts.append(viz_ts_ctxt)

    viz_prod_type_ctxt = ParameterContext(name='viz_product_type', param_type=ArrayType())
    contexts.append(viz_prod_type_ctxt)

    image_obj_ctxt = ParameterContext(name='image_obj', param_type=ArrayType())
    contexts.append(image_obj_ctxt)

    image_name_ctxt = ParameterContext(name='image_name', param_type=ArrayType())
    contexts.append(image_name_ctxt)

    content_type_ctxt = ParameterContext(name='content_type', param_type=ArrayType())
    contexts.append(content_type_ctxt)

    gdt_ctxt = ParameterContext(name='google_dt_components', param_type=RecordType())
    contexts.append(gdt_ctxt)

    mpl_ctxt = ParameterContext(name='mpl_graph', param_type=RecordType())
    contexts.append(mpl_ctxt)

    dummy_ctxt = ParameterContext(name='dummy', param_type=QuantityType(value_encoding=np.int64))
    contexts.append(dummy_ctxt)
    
    return contexts
    
if __name__ == '__main__':
    import sys
    sys.stderr.write('This plugin is not meant to be run')

