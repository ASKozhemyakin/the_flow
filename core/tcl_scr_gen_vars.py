import sys, os, glob, shutil
from messages import Messages


class TclScrGen_vars(Messages):

    def __init__(self,
                 step_dir,
                 step_table,
                 tf_run_dir_scripts,
                 tf_run_dir_work_tmp,
                 tf_tmp_file_steps_import,
                 tf_tmp_step_table,
                 flow_name,
                 tf_var_table,
                 tf_var_flow_table,
                 tf_var_common_table,
                 tf_var_mmmc_table,
                 mmmc_sdc_mode_table,
                 tf_run_dir_in_cfg
                 ):
        self.step_dir = step_dir
        self.step_table = step_table
        self.tf_run_dir_scripts = tf_run_dir_scripts
        self.tf_run_dir_work_tmp = tf_run_dir_work_tmp
        self.tf_tmp_file_steps_import = tf_tmp_file_steps_import
        self.tf_tmp_step_table = tf_tmp_step_table
        self.flow_name = flow_name
        self.tf_var_table = tf_var_table
        self.tf_var_flow_table = tf_var_flow_table
        self.tf_var_common_table = tf_var_common_table
        self.tf_var_mmmc_table = tf_var_mmmc_table
        self.mmmc_sdc_mode_table = mmmc_sdc_mode_table
        self.tf_run_dir_in_cfg = tf_run_dir_in_cfg

    def create_vars_config(self):

        original_stdout = sys.stdout

        tf_vars_config_tcl_file = self.tf_run_dir_in_cfg + '/vars_config.tcl'

        if self.tf_file_exists_check(tf_vars_config_tcl_file) == 'True':
            os.remove(tf_vars_config_tcl_file)

        with open(tf_vars_config_tcl_file, 'a') as f:
            sys.stdout = f

            print('# Flow type')
            print('set FLOW \"' + self.flow_name + '\"')
            print('')

            print('# Variables from tf_var_common.tf_var_common_table')
            for i in range(len(self.tf_var_common_table)):
                list_ = ''
                for j in range(1, len(self.tf_var_common_table[i])):
                    if list_ == '':
                        list_ = self.tf_var_common_table[i][j]
                    else:
                        list_ = list_ + ' ' + self.tf_var_common_table[i][j]
                if self.tf_var_common_table[i][0] != '':
                    print('set ' + self.tf_var_common_table[i][0] + ' \"' + list_ + '\"')
            print('')

            print('# Variables from tf_var.tf_var_table')
            for i in range(len(self.tf_var_table)):
                list_ = ''
                for j in range(1, len(self.tf_var_table[i])):
                    if list_ == '':
                        list_ = self.tf_var_table[i][j]
                    else:
                        list_ = list_ + ' ' + self.tf_var_table[i][j]
                if self.tf_var_table[i][0] != '':
                    print('set ' + self.tf_var_table[i][0] + ' \"' + list_ + '\"')
            print('')

            print('# Variables from tf_var.tf_var_' + self.flow_name + '_table')
            if self.tf_var_flow_table != '':
                for i in range(len(self.tf_var_flow_table)):
                    list_ = ''
                    for j in range(1, len(self.tf_var_flow_table[i])):
                        if list_ == '':
                            list_ = self.tf_var_flow_table[i][j]
                        else:
                            list_ = list_ + ' ' + self.tf_var_flow_table[i][j]
                    if self.tf_var_flow_table[i][0] != '':
                        print('set ' + self.tf_var_flow_table[i][0] + ' \"' + list_ + '\"')
            print('')

            print('# MMMC presets from tf_var.tf_var_mmmc_table')
            list_ = ''
            for i in range(0, len(self.tf_var_mmmc_table)):
                if list_ == '':
                    list_ = self.tf_var_mmmc_table[i]
                else:
                    list_ = list_ + ' ' + self.tf_var_mmmc_table[i]
            print('set MMMC_PRESETS \"' + list_ + '\"')
            print('')

            print('# MMMC sdc modes')
            list_ = ''
            for i in range(len(self.mmmc_sdc_mode_table)):
                if list_ == '':
                    list_ = self.mmmc_sdc_mode_table[i][0]
                else:
                    list_ = list_ + ' ' + self.mmmc_sdc_mode_table[i][0]
            print('set MMMC_SDC_MODES \"' + list_ + '\"')
            print('')

        sys.stdout = original_stdout

    def run(self):
        shutil.rmtree(self.tf_run_dir_work_tmp)
        os.mkdir(self.tf_run_dir_work_tmp)

        sys.path.append(self.tf_run_dir_work_tmp)

        self.create_vars_config()
