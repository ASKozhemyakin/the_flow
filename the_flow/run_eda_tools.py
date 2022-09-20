import os
import time
import global_tf_vars
import common_func
import tf_var


def run_eda_tools():

    if global_tf_vars.tf_is_syn == 1:
        for j in range(0, len(tf_var.tf_step_syn_table)):
            if tf_var.tf_step_syn_table[j][0] == 0:
                common_func.tf_info('start to execute ' + tf_var.tf_step_syn_table[j][1] + ' step')
                t = time.time()
                if global_tf_vars.tf_use_xterm == 1:
                    os.system(common_func.tf_run_eda_with_xterm('genus -f ../scripts/' +
                                                                tf_var.tf_step_syn_table[j][1] +
                                                                '.tcl -log ../logs/' +
                                                                tf_var.tf_step_syn_table[j][1] +
                                                                '.log -overwrite'))
                else:
                    os.system('genus -f ../scripts/' +
                              tf_var.tf_step_syn_table[j][1] +
                              '.tcl -log ../logs/' +
                              tf_var.tf_step_syn_table[j][1] +
                              '.log -overwrite')
                runtime = time.time() - t
                common_func.tf_info('finish to execute ' + tf_var.tf_step_syn_table[j][1] +
                                    ' step. runtime: ' + str(runtime // 60) + ' min')
            elif common_func.tf_file_exists_check('../db/' + tf_var.tf_step_syn_table[j - 1][1] + '.db') == \
                    'True':
                common_func.tf_info('start to execute ' + tf_var.tf_step_syn_table[j][1] + ' step')
                t = time.time()
                if global_tf_vars.tf_use_xterm == 1:
                    os.system(common_func.tf_run_eda_with_xterm('genus -f ../scripts/' +
                                                                tf_var.tf_step_syn_table[j][1] +
                                                                '.tcl -log ../logs/' +
                                                                tf_var.tf_step_syn_table[j][1] +
                                                                '.log -overwrite'))
                else:
                    os.system('genus -f ../scripts/' +
                              tf_var.tf_step_syn_table[j][1] +
                              '.tcl -log ../logs/' +
                              tf_var.tf_step_syn_table[j][1] +
                              '.log -overwrite')
                runtime = time.time() - t
                common_func.tf_info('finish to execute ' + tf_var.tf_step_syn_table[j][1] +
                                    ' step. runtime: ' + str(runtime // 60) + ' min')
            else:
                common_func.tf_error('previous step db doesn\'t exist')
                exit('exit with error')
    elif global_tf_vars.tf_is_impl == 1:
        for j in range(0, len(tf_var.tf_step_impl_table)):
            if tf_var.tf_step_impl_table[j][0] == 0:
                common_func.tf_info('start to execute ' + tf_var.tf_step_impl_table[j][1] + ' step')
                t = time.time()
                if global_tf_vars.tf_use_xterm == 1:
                    os.system(common_func.tf_run_eda_with_xterm('innovus -stylus -file ../scripts/' +
                                                                tf_var.tf_step_impl_table[j][1] +
                                                                '.tcl -log ../logs/' +
                                                                tf_var.tf_step_impl_table[j][1] +
                                                                '.log -overwrite'))
                else:
                    os.system('innovus -stylus -file ../scripts/' +
                              tf_var.tf_step_impl_table[j][1] +
                              '.tcl -log ../logs/' +
                              tf_var.tf_step_impl_table[j][1] +
                              '.log -overwrite')
                runtime = time.time() - t
                common_func.tf_info('finish to execute ' + tf_var.tf_step_impl_table[j][1] +
                                    ' step. runtime: ' + str(runtime // 60) + ' min')
            elif os.path.isdir('../db/' + tf_var.tf_step_impl_table[j - 1][1] + '.db'):
                common_func.tf_info('start to execute ' + tf_var.tf_step_impl_table[j][1] + ' step')
                t = time.time()
                if global_tf_vars.tf_use_xterm == 1:
                    os.system(common_func.tf_run_eda_with_xterm('innovus -stylus -file ../scripts/' +
                                                                tf_var.tf_step_impl_table[j][1] +
                                                                '.tcl -log ../logs/' +
                                                                tf_var.tf_step_impl_table[j][1] +
                                                                '.log -overwrite'))
                else:
                    os.system('innovus -stylus -file ../scripts/' +
                              tf_var.tf_step_impl_table[j][1] +
                              '.tcl -log ../logs/' +
                              tf_var.tf_step_impl_table[j][1] +
                              '.log -overwrite')
                runtime = time.time() - t
                common_func.tf_info('finish to execute ' + tf_var.tf_step_impl_table[j][1] +
                                    ' step. runtime: ' + str(runtime // 60) + ' min')
            else:
                common_func.tf_error('previous step db doesn\'t exist')
                exit('exit with error')
    elif global_tf_vars.tf_is_atpg == 1:
        for j in range(0, len(tf_var.tf_step_atpg_table)):
            common_func.tf_info('start to execute ' + tf_var.tf_step_atpg_table[j][1] + ' step')
            t = time.time()
            if global_tf_vars.tf_use_xterm == 1:
                os.system(common_func.tf_run_eda_with_xterm('modus -f ../scripts/' +
                                                            tf_var.tf_step_atpg_table[j][1] +
                                                            '.tcl -log ../logs/' +
                                                            tf_var.tf_step_atpg_table[j][1] +
                                                            '.log'))
            else:
                os.system('modus -f ../scripts/' +
                          tf_var.tf_step_atpg_table[j][1] +
                          '.tcl -log ../logs/' +
                          tf_var.tf_step_atpg_table[j][1] +
                          '.log')
            runtime = time.time() - t
            common_func.tf_info('finish to execute ' + tf_var.tf_step_atpg_table[j][1] +
                                ' step. runtime: ' + str(runtime // 60) + ' min')