#!/usr/bin/python -OO
# -*- coding: UTF-8 -*-
# Copyright 2011 The SABnzbd-Team <team@sabnzbd.org>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

"""
sabnzbd.skintext - Language strings used in the templates
"""

SKIN_TEXT = {

# Special texts
    'stage-download'     : TT('Download'),
    'stage-repair'       : TT('Repair'),
    'stage-filejoin'     : TT('Join files'),
    'stage-unpack'       : TT('Unpack'),
    'stage-script'       : TT('Script'),

    'post-Completed'     : TT('Completed'),
    'post-Failed'        : TT('Failed'),
    'post-Queued'        : TT('Queued'),
    'post-Paused'        : TT('Paused'),
    'post-Repairing'     : TT('Repairing...'),
    'post-Extracting'    : TT('Extracting...'),
    'post-Moving'        : TT('Moving...'),
    'post-Running'       : TT('Running script...'),
    'post-Fetching'      : TT('Fetching extra blocks...'),
    'post-QuickCheck'    : TT('Quick Check...'),
    'post-Verifying'     : TT('Verifying...'),

    'sch-frequency'      : TT('Frequency'),
    'sch-action'         : TT('Action'),
    'sch-arguments'      : TT('Arguments'),
    'sch-task'           : TT('Task'),
    'sch-disable_server' : TT('disable server'),
    'sch-enable_server'  : TT('enable server'),
    'sch-resume'         : TT('Resume'),
    'sch-pause'          : TT('Pause'),
    'sch-shutdown'       : TT('Shutdown'),
    'sch-restart'        : TT('Restart'),
    'sch-speedlimit'     : TT('Speedlimit'),
    'sch-pause_all'      : TT('Pause All'),
    'sch-pause_post'     : TT('Pause post-processing'),
    'sch-resume_post'    : TT('Resume post-processing'),
    'sch-scan_folder'    : TT('Scan watched folder'),
    'sch-rss_scan'       : TT('Read RSS feeds'),

# General texts
    'default' : TT('Default'),
    'none' : TT('None'),
    'KBs' : TT('KB/s'),
    'MB' : TT('MB'),
    'GB' : TT('GB'),
    'hour' : TT('hour'),
    'hours' : TT('hours'),
    'minute' : TT('min'),
    'minutes' : TT('mins'),
    'second' : TT('sec'),
    'seconds' : TT('seconds'),
    'day' : TT('day'),
    'days' : TT('days'),
    'month' : TT('Month'),
    'year' : TT('Year'),
    'daily' : TT('Daily'),
    'monday' : TT('Monday'),
    'tuesday' : TT('Tuesday'),
    'wednesday' : TT('Wednesday'),
    'thursday' : TT('Thursday'),
    'friday' : TT('Friday'),
    'saturday' : TT('Saturday'),
    'sunday' : TT('Sunday'),
    'day-of-month' : TT('Day of month'),
    'thisWeek' : TT('This week'),
    'thisMonth' : TT('This month'),
    'today' : TT('Today'),
    'total' : TT('Total'),

# General template elements
    'signOn' : TT('The automatic usenet download tool'),
    'button-save' : TT('Save'),
    'queued' : TT('Queued'),
    'button-back' : TT('Back'),
    'button-x' : TT('X'),
    'confirm' : TT('Are you sure?'),
    'delFiles' : TT('Delete all downloaded files?'),

# Header
    'menu-home' : TT('Home'),
    'menu-queue' : TT('Queue'),
    'menu-history' : TT('History'),
    'menu-config' : TT('Config'),
    'menu-cons' : TT('Status'),
    'menu-help' : TT('Help'),
    'menu-wiki' : TT('Wiki'),
    'menu-forums' : TT('Forum'),
    'menu-irc' : TT('IRC'),
    'cmenu-general' : TT('General'),
    'cmenu-folders' : TT('Folders'),
    'cmenu-switches' : TT('Switches'),
    'cmenu-servers' : TT('Servers'),
    'cmenu-scheduling' : TT('Scheduling'),
    'cmenu-rss' : TT('RSS'),
    'cmenu-email' : TT('Email'),
    'cmenu-newzbin' : TT('Index Sites'),
    'cmenu-cat' : TT('Categories'),
    'cmenu-sorting' : TT('Sorting'),

# Footer
    'ft-download' : TT('Download Dir'),
    'ft-complete' : TT('Complete Dir'),
    'ft-speed' : TT('Download speed'),
    'ft-queued' : TT('Queued'),
    'ft-paused' : TT('PAUSED'),
    'ft-buffer@2' : TT('Cached %s articles (%s)'),
    'ft-sysload' : TT('Sysload'),
    'ft-warning' : TT('WARNINGS'),
    'ft-newRelease@1' : TT('New release %s available at'),

# Main page
    'addNewJobs' : TT('Add new downloads'),
    'shutdownOK?' : TT('Are you sure you want to shutdown SABnzbd?'),
    'link-shutdown' : TT('Shutdown'),
    'link-pause' : TT('Pause'),
    'link-resume' : TT('Resume'),
    'button-add' : TT('Add'),
    'add' : TT('Add'),
    'reportId' : TT('Report-id'),
    'addFile' : TT('Add File'),
    'category' : TT('Category'),
    'pp' : TT('Processing'),
    'script' : TT('Script'),
    'priority' : TT('Priority'),
    'pp-none' : TT('Download'),
    'pp-repair' : TT('+Repair'),
    'pp-unpack' : TT('+Unpack'),
    'pp-delete' : TT('+Delete'),
    'pp-n' : TT('&nbsp;'),
    'pp-r' : TT('R'),
    'pp-u' : TT('U'),
    'pp-d' : TT('D'),
    'pr-force' : TT('Force'),
    'pr-normal' : TT('Normal'),
    'pr-high' : TT('High'),
    'pr-low' : TT('Low'),
    'pr-paused' : TT('Paused'),
    'enterURL' : TT('Enter URL'),
    'enterID' : TT('&nbsp;or Report ID'),

# Queue page
    'link-sortByName' : TT('Sort by name'),
    'link-sortByAge' : TT('Sort by age'),
    'link-sortBySize' : TT('Sort by size'),
    'link-hideFiles' : TT('Hide files'),
    'link-showFiles' : TT('Show files'),
    'onQueueFinish' : TT('On queue finish'),
    'shutdownPc' : TT('Shutdown PC'),
    'standbyPc' : TT('Standby PC'),
    'hibernatePc' : TT('Hibernate PC'),
    'shutdownSab' : TT('Shutdown SABnzbd'),
    'speedLimit' : TT('Speed Limit'),
    'pauseFor' : TT('Pause for'),
    'mode' : TT('Processing'),
    'order' : TT('Order'),
    'name' : TT('Name'),
    'remainTotal' : TT('Remain/Total'),
    'eta' : TT('ETA'),
    'age' : TT('AGE'),
    'button-del' : TT('Del'),
    'button-resume' : TT('Resume'),
    'button-pause' : TT('Pause'),
    'button-retry' : TT('Retry'),
    'eoq-actions' : TT('Actions'),
    'eoq-scripts' : TT('Scripts'),
    'purgeQueue' : TT('Purge Queue'),
    'purgeQueueConf' : TT('Delete all items from the queue?'),
    'purgeNZBs' : TT('Purge NZBs'),
    'purgeNZBs-Files' : TT('Purge NZBs & Delete Files'),
    'removeNZB' : TT('Remove NZB'),
    'removeNZB-Files' : TT('Remove NZB & Delete Files'),

# History page
    'purgeHist' : TT('Purge History'),
    'purgeHistFailed' : TT('Purge Failed History'),
    'purgeHistConf' : TT('Delete all completed items from History?'),
    'purgeHistFailedConf' : TT('Delete all failed items from History?'),
    'hideDetails' : TT('Hide details'),
    'showDetails' : TT('Show details'),
    'sizeHist' : TT('History Size'),
    'showFailedHis' : TT('Show Failed'),
    'showAllHis' : TT('Show all'),
    'completed' : TT('Completed'),
    'size' : TT('Size'),
    'status' : TT('Status'),
    'purgeFailed' : TT('Purge Failed NZBs'),
    'purgeFailed-Files' : TT('Purge Failed NZBs & Delete Files'),
    'purgeCompl' : TT('Purge Completed NZBs'),
    'opt-extra-NZB' : TT('Optional Supplemental NZB'),


# Connections page
    'link-forceDisc' : TT('Force Disconnect'),
    'askTestEmail' : TT('This will send a test email to your account.'),
    'link-showLog' : TT('Show Logging'),
    'link-showWeblog' : TT('Show Weblogging'),
    'link-testEmail' : TT('Test Email'),
    'logging' : TT('Logging'),
    'log-errWarn' : TT('Errors/Warning'),
    'log-info' : TT('+ Info'),
    'log-debug' : TT('+ Debug'),
    'connections' : TT('Connections'),
    'thread' : TT('Thread'),
    'emailResult' : TT('Email Test Result'),
    'lastWarnings' : TT('Latest Warnings'),
    'clearWarnings' : TT('clear'),
    'server-blocked' : TT('Unblock'),
    'article-id' : TT('Article identifier'),
    'file-set' : TT('File set'),
    'warn-when' : TT('When'),
    'warn-type' : TT('Type'),
    'warning' : TT('Warning'),
    'warnings' : TT('Warnings'),
    'enabled' : TT('Enabled'),

# Configuration
    'configuration' : TT('Configuration'),
    'confgFile' : TT('Config File'),
    'explain-Restart' : TT('The button below will restart SABnzbd.<br />Use it when you think the program has a stability problem.<br />Downloading will be paused before the restart and resume afterwards.'),
    'button-restart' : TT('Restart'),
    'explain-orphans' : TT('There are orphaned jobs in the download folder.<br/>You can choose to delete them (including files) or send them back to the queue.'),
    'button-repair' : TT('Repair'),
    'explain-Repair' : TT('The "Repair" button will restart SABnzbd and do a complete<br />reconstruction of the queue content, preserving already downloaded files.<br />This will modify the queue order.'),
    'version' : TT('Version'),
    'uptime' : TT('Uptime'),
    'backup' : TT('Backup'),

# Config->General
    'generalConfig' : TT('General configuration'),
    'restartRequired' : TT('Changes will require a SABnzbd restart!'),
    'webServer' : TT('SABnzbd Web Server'),
    'opt-host' : TT('SABnzbd Host'),
    'explain-host' : TT('Host SABnzbd should listen on.'),
    'opt-port' : TT('SABnzbd Port'),
    'explain-port' : TT('Port SABnzbd should listen on.'),
    'opt-web_dir' : TT('Web Interface'),
    'explain-web_dir' : TT('Choose a skin.'),
    'opt-web_dir2' : TT('Secondary Web Interface'),
    'explain-web_dir2' : TT('Activate an alternative skin.'),
    'webAuth' : TT('Web server authentication'),
    'opt-web_username' : TT('SABnzbd Username'),
    'explain-web_username' : TT('Optional authentication username.'),
    'opt-web_password' : TT('SABnzbd Password'),
    'explain-web_password' : TT('Optional authentication password.'),
    'httpsSupport' : TT('HTTPS Support'),
    'opt-enable_https' : TT('Enable HTTPS'),
    'opt-notInstalled' : TT('not installed'),
    'explain-enable_https' : TT('Enable accessing the interface from a HTTPS address.'),
    'opt-https_port' : TT('HTTPS Port'),
    'explain-https_port' : TT('If empty, the standard port will only listen to HTTPS.'),
    'opt-https_cert' : TT('HTTPS Certificate'),
    'explain-https_cert' : TT('File name or path to HTTPS Certificate.'),
    'opt-https_key' : TT('HTTPS Key'),
    'explain-https_key' : TT('File name or path to HTTPS Key.'),
    'tuning' : TT('Tuning'),
    'opt-refresh_rate' : TT('Queue auto refresh interval:'),
    'explain-refresh_rate' : TT('Refresh interval of the queue web-interface page(sec, 0= none).'),
    'opt-rss_rate' : TT('RSS Checking Interval'),
    'explain-rss_rate' : TT('Checking interval (in minutes, at least 15). Not active when you use the Scheduler!'),
    'opt-bandwidth_limit' : TT('Download Speed Limit'),
    'explain-bandwidth_limit' : TT('Download rate limit (in KB/s - kilobytes per second).'),
    'opt-cache_limitstr' : TT('Article Cache Limit'),
    'explain-cache_limitstr' : TT('Cache articles in memory to reduce disk access.<br /><i>In bytes, optionally follow with K,M,G. For example: "64M" or "128M"</i>'),
    'opt-cleanup_list' : TT('Cleanup List'),
    'explain-cleanup_list' : TT('List of file extensions that should be deleted after download.<br />For example: <b>.nfo</b> or <b>.nfo, .sfv</b>'),
    'button-saveChanges' : TT('Save Changes'),
    'opt-language' : TT('Language'),
    'explain-language' : TT('Select a web interface language.'),
    'opt-apikey' : TT('API Key'),
    'explain-apikey' : TT('This key is used to give 3rd party programs access to SABnzbd.'),
    'button-apikey' : TT('Generate New Key'),
    'opt-disableApikey' : TT('Disable API-key'),
    'explain-disableApikey' : TT('Do not require the API key.'),
    'explain-disableApikeyWarn' : TT('USE AT YOUR OWN RISK!'),

# Config->Folders
    'folderConfig' : TT('Folder configuration'),
    'explain-folderConfig' : TT('<em>NOTE:</em> Folders will be created automatically when Saving. You may use absolute paths to save outside of the default folders.'),
    'userFolders' : TT('User Folders'),
    'in' : TT('In'),
    'opt-download_dir' : TT('Temporary Download Folder'),
    'explain-download_dir' : TT('Location to store unprocessed downloads.<br /><i>Can only be changed when queue is empty.</i>'),
    'opt-download_free' : TT('Minimum Free Space for Temporary Download Folder'),
    'explain-download_free' : TT('Auto-pause when free space is beneath this value.<br /><i>In bytes, optionally follow with K,M,G,T. For example: "800M" or "8G"</i>'),
    'opt-complete_dir' : TT('Completed Download Folder'),
    'explain-complete_dir' : TT('Location to store finished, fully processed downloads.<br /><i>Can be overruled by user-defined categories.</i>'),
    'opt-permissions' : TT('Permissions for completed downloads'),
    'explain-permissions' : TT('Set permissions pattern for completed files/folders.<br /><i>In octal notation. For example: "755" or "777"</i>'),
    'opt-dirscan_dir' : TT('Watched Folder'),
    'explain-dirscan_dir' : TT('Folder to monitor for .nzb files.<br /><i>Also scans .zip .rar and .tar.gz archives for .nzb files.</i>'),
    'opt-dirscan_speed' : TT('Watched Folder Scan Speed'),
    'explain-dirscan_speed' : TT('Number of seconds between scans for .nzb files.'),
    'opt-script_dir' : TT('Post-Processing Scripts Folder'),
    'explain-script_dir' : TT('Folder containing user scripts for post-processing.'),
    'opt-email_dir' : TT('Email Templates Folder'),
    'explain-email_dir' : TT('Folder containing user-defined email templates.'),
    'opt-password_file' : TT('Password file'),
    'explain-password_file' : TT('File containing all passwords to be tried on encrypted RAR files.'),
    'systemFolders' : TT('System Folders'),
    'opt-admin_dir' : TT('Administrative Folder'),
    'explain-admin_dir' : TT('Location for queue admin and history database.<br /><i>Can only be changed when queue is empty.</i><br /><i>Data will <b>not</b> be moved.</i><br /><i>Requires SABnzbd restart!</i>'),
    'opt-log_dir' : TT('Log Folder'),
    'explain-log_dir' : TT('Location of log files for SABnzbd.<br /><i>Requires SABnzbd restart!</i>'),
    'opt-nzb_backup_dir' : TT('.nzb Backup Folder'),
    'explain-nzb_backup_dir' : TT('Location where .nzb files will be stored.'),
    'base-folder' : TT('Default Base Folder'),

# Config->Switches
    'switchesConfig' : TT('Switches configuration'),
    'processingSwitches' : TT('Processing Switches'),
    'opt-quick_check' : TT('Enable Quick Check'),
    'explain-quick_check' : TT('Skip par2 checking when files are 100% valid.'),
    'opt-enable_unrar' : TT('Enable Unrar'),
    'explain-enable_unrar' : TT('Enable built-in unrar functionality.'),
    'opt-enable_unzip' : TT('Enable Unzip'),
    'explain-enable_unzip' : TT('Enable built-in unzip functionality.'),
    'opt-enable_filejoin' : TT('Enable Filejoin'),
    'explain-enable_filejoin' : TT('Join files ending in .001, .002 etc. into one file.'),
    'opt-enable_tsjoin' : TT('Enable TS Joining'),
    'explain-ts_join' : TT('Join files ending in .001.ts, .002.ts etc. into one file.'),
    'opt-enable_par_cleanup' : TT('Enable Par Cleanup'),
    'explain-enable_par_cleanup' : TT('Cleanup par files (if verifiying/repairing succeded).'),
    'opt-fail_on_crc' : TT('Fail on yEnc CRC Errors'),
    'explain-fail_on_crc' : TT('Use backup servers on yEnc crc errors.'),
    'opt-top_only' : TT('Only Get Articles for Top of Queue'),
    'explain-top_only' : TT('Enable for less memory usage. Disable to prevent slow jobs from blocking the queue.'),
    'opt-safe_postproc' : TT('Post-Process Only Verified Jobs'),
    'explain-safe_postproc' : TT('Only perform post-processing on jobs that passed all PAR2 checks.'),
    'opt-pause_on_pwrar' : TT('Pause job when encrypted RAR is downloaded'),
    'explain-pause_on_pwrar' : TT('You\'ll need to set a password and resume the job.'),
    'opt-no_dupes' : TT('Prevent Duplicate Downloads'),
    'explain-no_dupes' : TT('Skip a job if a backed-up .nzb with the same name exists.'),
    'opt-sfv_check' : TT('Enable SFV-based checks'),
    'explain-sfv_check' : TT('Do an extra verification based on SFV files.'),
    'opt-folder_rename' : TT('Enable folder rename'),
    'explain-folder_rename' : TT('Use temporary names during post processing. Disable when your system doesn\'t handle that properly.'),
    'opt-dirscan_opts' : TT('Default Post-Processing'),
    'explain-dirscan_opts' : TT('Used when no post-processing is defined by the category.'),
    'opt-dirscan_script' : TT('Default User Script'),
    'explain-dirscan_script' : TT('Used when no user script is defined by the category.'),
    'opt-pre_script' : TT('Pre-queue user script'),
    'explain-pre_script' : TT('Used before an NZB enters the queue.'),
    'opt-dirscan_priority' : TT('Default Priority'),
    'explain-dirscan_priority' : TT('Used when no priority is defined by the category.'),
    'opt-par2_multicore' : TT('Enable MultiCore Par2'),
    'explain-par2_multicore' : TT('Read the Wiki Help on this!'),
    'opt-par_option' : TT('Extra PAR2 Parameters'),
    'explain-par_option' : TT('Read the Wiki Help on this!'),
    'opt-nice' : TT('Nice Parameters'),
    'explain-nice' : TT('Read the Wiki Help on this!'),
    'opt-ionice' : TT('IONice Parameters'),
    'explain-ionice' : TT('Read the Wiki Help on this!'),
    'otherSwitches' : TT('Other Switches'),
    'opt-auto_disconnect' : TT('Disconnect on Empty Queue'),
    'explain-auto_disconnect' : TT('Disconnect from Usenet server(s) when queue is empty or paused.'),
    'opt-send_group' : TT('Send Group'),
    'explain-send_group' : TT('Send group command before requesting articles.'),
    'opt-auto_sort' : TT('Sort by Age'),
    'explain-auto_sort' : TT('Automatically sort items by (average) age.'),
    'opt-check_new_rel' : TT('Check for New Release'),
    'explain-check_new_rel' : TT('Weekly check for new SABnzbd release.'),
    'opt-replace_spaces' : TT('Replace Spaces in Foldername'),
    'explain-replace_spaces' : TT('Replace spaces with underscores in folder names.'),
    'opt-replace_dots' : TT('Replace dots in Foldername'),
    'explain-replace_dots' : TT('Replace dots with spaces in folder names.'),
    'opt-replace_illegal' : TT('Replace Illegal Characters in Folder Names'),
    'explain-replace_illegal' : TT('Replace illegal characters in folder names by equivalents (otherwise remove).'),
    'opt-auto_browser' : TT('Launch Browser on Startup'),
    'explain-auto_browser' : TT('Launch the default web browser when starting SABnzbd.'),
    'opt-pause_on_post_processing' : TT('Pause Downloading During Post-Processing'),
    'explain-pause_on_post_processing' : TT('Pauses downloading at the start of post processing and resumes when finished.'),
    'opt-ignore_samples' : TT('Ignore Samples'),
    'explain-ignore_samples' : TT('Filter out sample files (e.g. video samples).'),
    'igsam-off' : TT('Off'),
    'igsam-del' : TT('Delete after download'),
    'igsam-not' : TT('Do not download'),
    'opt-ssl_type' : TT('SSL type'),
    'explain-ssl_type' : TT('Use V23 unless your provider requires otherwise!'),
    'opt-ampm' : TT('Use 12 hour clock (AM/PM)'),
    'explain-ampm' : TT('Show times in AM/PM notation (does not affect scheduler).'),
    'swtag-general' : TT('General'),
    'swtag-server' : TT('Server'),
    'swtag-queue' : TT('Queue'),
    'swtag-pp' : TT('Post processing'),
    'swtag-naming' : TT('Naming'),


# Config->Server
    'configServer' : TT('Server configuration'),
    'defServer' : TT('Server definition'),
    'addServer' : TT('Add Server'),
    'srv-host' : TT('Host'),
    'srv-port' : TT('Port'),
    'srv-username' : TT('Username'),
    'srv-password' : TT('Password'),
    'srv-timeout' : TT('Timeout'),
    'srv-connections' : TT('Connections'),
    'srv-retention' : TT('Retention time'),
    'srv-ssl' : TT('SSL'),
    'srv-fillserver' : TT('Backup server'),
    'srv-optional' : TT('Optional'),
    'srv-enable' : TT('Enable'),
    'button-addServer' : TT('Add Server'),
    'button-delServer' : TT('Remove Server'),
    'button-testServer' : TT('Test Server'),
    'srv-testing' : TT('Testing server details...'),
    'srv-testHint' : TT('Click below to test.'),
    'srv-bandwidth' : TT('Bandwidth'),

# Config->Scheduling
    'configSchedule' : TT('Scheduling configuration'),
    'addSchedule' : TT('Add Schedule'),
    'sch-frequency' : TT('Frequency'),
    'sch-action' : TT('Action'),
    'sch-arguments' : TT('Arguments'),
    'button-addSchedule' : TT('Add Schedule'),
    'button-delSchedule' : TT('Remove'),
    'currentSchedules' : TT('Current Schedules'),
    'sch-resume' : TT('Resume'),
    'sch-pause' : TT('Pause'),
    'sch-shutdown' : TT('Shutdown'),
    'sch-restart' : TT('Restart'),

# Config->RSS
    'configRSS' : TT('RSS Configuration'),
    'newFeedURI' : TT('New Feed URL'),
    'explain-RSS' : TT('The checkbox next to the feed name should be ticked for the feed to be enabled and be automatically checked for new items.<br />The checking frequency is in the General page of the configuration.<br />When a feed is added, it will only pick up new items and not anything already in the RSS feed unless you press "Force Download".'),
    'feed' : TT('Feed'),
    'button-delFeed' : TT('Delete Feed'),
    'button-preFeed' : TT('Read Feed'),
    'button-forceFeed' : TT('Force Download'),
    'rss-order' : TT('Order'),
    'rss-type' : TT('Type'),
    'rss-filter' : TT('Filter'),
    'rss-skip' : TT('Skip'),
    'rss-accept' : TT('Accept'),
    'rss-reject' : TT('Reject'),
    'rss-must' : TT('Requires'),
    'rss-mustcat' : TT('RequiresCat'),
    'rss-delFilter' : TT('X'),
    'rss-matched' : TT('Matched'),
    'rss-notMatched' : TT('Not matched'),
    'rss-done' : TT('Downloaded'),
    'link-download' : TT('Download'),

# Config->Email
    'configEmail' : TT('Email Notification'),
    'emailOptions' : TT('Email Options'),
    'opt-email_endjob' : TT('Email Notification On Job Completion'),
    'email-never' : TT('Never'),
    'email-always' : TT('Always'),
    'email-errorOnly' : TT('Error-only'),
    'opt-email_full' : TT('Disk Full Notifications'),
    'explain-email_full' : TT('Send email when disk is full and SABnzbd is paused.'),
    'opt-email_rss' : TT('Send RSS notifications'),
    'explain-email_rss' : TT('Send email when an RSS feed adds jobs to the queue.'),
    'emailAccount' : TT('Email Account Settings'),
    'opt-email_server' : TT('SMTP Server'),
    'explain-email_server' : TT('Set your ISP\'s server for outgoing email.'),
    'opt-email_to' : TT('Email Recipient'),
    'explain-email_to' : TT('Email address to send the email to.'),
    'opt-email_from' : TT('Email Sender'),
    'explain-email_from' : TT('Who should we say sent the email?'),
    'opt-email_account' : TT('OPTIONAL Account Username'),
    'explain-email_account' : TT('For authenticated email, account name.'),
    'opt-email_pwd' : TT('OPTIONAL Account Password'),
    'explain-email_pwd' : TT('For authenticated email, password.'),

# Config->Newzbin
    'explain-newzbin' : TT('If you have an account at <strong>www.newzbin.com</strong>, you can enter your account info here.<br />This will unlock extra functionality.'),
    'accountInfo' : TT('Account info'),
    'opt-username_newzbin' : TT('Newzbin Username'),
    'explain-username_newzbin' : TT('Set your account username here.'),
    'opt-password_newzbin' : TT('Newzbin Password'),
    'explain-password_newzbin' : TT('Set your account password here.'),
    'newzbinBookmarks' : TT('Bookmark Processing'),
    'opt-newzbin_bookmarks' : TT('Auto-Fetch Bookmarks'),
    'explain-newzbin_bookmarks' : TT('Automatically retrieve jobs from your bookmarks.'),
    'link-getBookmarks' : TT('Get Bookmarks Now'),
    'link-HideBM' : TT('Hide Processed Bookmarks'),
    'link-ShowBM' : TT('Show Processed Bookmarks'),
    'opt-newzbin_unbookmark' : TT('Un-Bookmark If Download Complete'),
    'explain-newzbin_unbookmark' : TT('Remove from bookmark list when download is complete.'),
    'opt-bookmark_rate' : TT('Checking Interval'),
    'explain-bookmark_rate' : TT('In minutes (at least 15 min).'),
    'processedBM' : TT('Processed Bookmarks'),
    'explain-nzbmatrix' : TT('If you have an account at <strong>www.nzbmatrix.com</strong>, you can enter your account info here.<br />This is required if you want to use the RSS feeds of this site.'),
    'opt-username_matrix' : TT('NzbMatrix Username'),
    'explain-username_matrix' : TT('Set your account username here.'),
    'opt-apikey_matrix' : TT('NzbMatrix API key'),
    'explain-apikey_matrix' : TT('Set the NzbMatrix API key here.'),

# Config->Cat
    'configCat' : TT('User-defined categories'),
    'explain-configCat' : TT('Defines post-processing and storage.'),
    'explain-catTags' : TT('Use the "Groups / Indexer tags" column to map groups and tags to your categories.<br/>Wildcards are supported. Use comma\'s to seperate terms.'),
    'explain-relFolder' : TT('Relative folders are based on'),
    'catFolderPath' : TT('Folder/Path'),
    'catTags' : TT('Groups / Indexer tags'),
    'button-delCat' : TT('X'),

# Config->Sorting
    'configSort' : TT('Sorting configuration'),
    'seriesSorting' : TT('Series Sorting'),
    'opt-tvsort' : TT('Enable TV Sorting'),
    'explain-tvsort' : TT('Enable sorting and renaming of episodes.'),
    'sort-legenda' : TT('Pattern Key'),
    'button-clear' : TT('Clear'),
    'presetSort' : TT('Presets'),
    'example' : TT('Example'),
    'genericSort' : TT('Generic Sorting'),
    'opt-movieSort' : TT('Enable Movie Sorting'),
    'explain-movieSort' : TT('Enable generic sorting and renaming of files.'),
    'opt-movieExtra' : TT('Keep loose downloads in extra folders'),
    'explain-movieExtra' : TT('Enable if downloads are not put in their own folders.'),
    'affectedCat' : TT('Affected Categories'),
    'sort-meaning' : TT('Meaning'),
    'sort-pattern' : TT('Pattern'),
    'sort-result' : TT('Result'),
    'button-Season1x05' : TT('1x05 Season Folder'),
    'button-SeasonS01E05' : TT('S01E05 Season Folder'),
    'button-Ep1x05' : TT('1x05 Episode Folder'),
    'button-EpS01E05' : TT('S01E05 Episode Folder'),
    'sort-title' : TT('Title'),
    'movie-sp-name' : TT('Movie Name'),
    'movie-dot-name' : TT('Movie.Name'),
    'movie-us-name' : TT('Movie_Name'),
    'show-name' : TT('Show Name'),
    'show-sp-name' : TT('Show Name'),
    'show-dot-name' : TT('Show.Name'),
    'show-us-name' : TT('Show_Name'),
    'show-seasonNum' : TT('Season Number'),
    'show-epNum' : TT('Episode Number'),
    'ep-name' : TT('Episode Name'),
    'ep-sp-name' : TT('Episode Name'),
    'ep-dot-name' : TT('Episode.Name'),
    'ep-us-name' : TT('Episode_Name'),
    'fileExt' : TT('File Extension'),
    'extension' : TT('Extension'),
    'partNumber' : TT('Part Number'),
    'decade' : TT('Decade'),
    'orgFilename' : TT('Original Filename'),
    'orgDirname' : TT('Original Foldername'),
    'lowercase' : TT('Lower Case'),
    'TEXT' : TT('TEXT'),
    'text' : TT('text'),
    'sort-File' : TT('file'),
    'sort-Folder' : TT('folder'),
    'sortString' : TT('Sort String'),
    'multiPartLabel' : TT('Multi-part label'),
    'button-inFolders' : TT('In folders'),
    'button-noFolders' : TT('No folders'),
    'dateSorting' : TT('Date Sorting'),
    'opt-dateSort' : TT('Enable Date Sorting'),
    'explain-dateSort' : TT('Enable sorting and renaming of date named files.'),
    'button-ShowNameF' : TT('Show Name folder'),
    'button-YMF' : TT('Year-Month Folders'),
    'button-DailyF' : TT('Daily Folders'),

# NZO
    'nzoDetails' : TT('Edit NZB Details'),
    'nzoName' : TT('Name'),
    'nzo-delete' : TT('Delete'),
    'nzo-top' : TT('Top'),
    'nzo-up' : TT('Up'),
    'nzo-down' : TT('Down'),
    'nzo-bottom' : TT('Bottom'),
    'nzo-all' : TT('All'),
    'nzo-none' : TT('None'),
    'nzo-invert' : TT('Invert'),
    'nzo-filename' : TT('Filename'),
    'nzo-subject' : TT('Subject'),
    'nzo-age' : TT('Age'),
    'nzo-selection' : TT('Selection'),

# Internal texts

# Errors and Warnings
    'msg-path' : TT('Path'),
    'stage-download' : TT('Download'),
    'stage-repair' : TT('Repair'),
    'stage-filejoin' : TT('Join files'),
    'stage-unpack' : TT('Unpack'),
    'stage-script' : TT('Script'),

#Growl Messages

#OSX Menu
    'Mobile-confirm-delete' : TT('Are you sure you want to delete'),
    'Mobile-button-refresh' : TT('Refresh'),
    'Mobile-warnings' : TT('Warnings'),
    'Mobile-button-options' : TT('Options'),
    'Mobile-page' : TT('Page'),
    'Mobile-button-prev' : TT('Prev'),
    'Mobile-button-next' : TT('Next'),
    'Mobile-button-first' : TT('First'),
    'Mobile-button-last' : TT('Last'),
    'Mobile-button-close' : TT('Close'),
    'Mobile-button-pauseInterval' : TT('Set Pause Interval'),
    'Mobile-sort' : TT('Sort'),
    'Mobile-confirm-purgeQ' : TT('Purge the Queue?'),
    'Mobile-button-purgeQ' : TT('Purge Queue'),
    'Mobile-pauseInterval' : TT('Pause Interval'),
    'Mobile-pause5m' : TT('Pause for 5 minutes'),
    'Mobile-pause15m' : TT('Pause for 15 minutes'),
    'Mobile-pause30m' : TT('Pause for 30 minutes'),
    'Mobile-pause1h' : TT('Pause for 1 hour'),
    'Mobile-pause3h' : TT('Pause for 3 hours'),
    'Mobile-pause6h' : TT('Pause for 6 hours'),
    'Mobile-pause12h' : TT('Pause for 12 hours'),
    'Mobile-pause24h' : TT('Pause for 24 hours'),
    'Mobile-sortAgeAsc' : TT('Sort by Age <small>Oldest&rarr;Newest</small>'),
    'Mobile-sortAgeDesc' : TT('Sort by Age <small>Newest&rarr;Oldest</small>'),
    'Mobile-sortNameAsc' : TT('Sort by Name <small>A&rarr;Z</small>'),
    'Mobile-sortNameDesc' : TT('Sort by Name <small>Z&rarr;A</small>'),
    'Mobile-sortSizeAsc' : TT('Sort by Size <small>Smallest&rarr;Largest</small>'),
    'Mobile-sortSizeDesc' : TT('Sort by Size <small>Largest&rarr;Smallest</small>'),
    'Mobile-rename' : TT('Rename'),
    'Mobile-left' : TT('Left'),
    'Mobile-confirm-purgeH' : TT('Purge the History?'),
    'Mobile-button-purgeH' : TT('Purge History'),

#Plush skin
    'Plush-confirmWithoutSavingPrompt' : TT('Changes have not been saved, and will be lost.'),
    'Plush-cmenu-scheduling' : TT('Scheduling'),
    'Plush-confirm' : TT('Are you sure?'),
    'Plush-openSourceURL' : TT('Open Source URL'),
    'Plush-openInfoURL' : TT('Open Informational URL'),
    'Plush-path' : TT('Path'),
    'Plush-storage' : TT('Storage'),
    'Plush-viewScriptLog' : TT('View Script Log'),
    'Plush-prev' : TT('Prev'),
    'Plush-next' : TT('Next'),
    'Plush-confirmPurgeH' : TT('Purge the History?'),
    'Plush-enableJavascript' : TT('You must enable JavaScript for Plush to function!'),
    'Plush-addnzb' : TT('Add NZB'),
    'Plush-button-refresh' : TT('Refresh'),
    'Plush-options' : TT('Options'),
    'Plush-plushoptions' : TT('Plush Options'),
    'Plush-updateAvailable' : TT('Update Available!'),
    'Plush-pause5m' : TT('Pause for 5 minutes'),
    'Plush-pause15m' : TT('Pause for 15 minutes'),
    'Plush-pause30m' : TT('Pause for 30 minutes'),
    'Plush-pause1h' : TT('Pause for 1 hour'),
    'Plush-pause3h' : TT('Pause for 3 hours'),
    'Plush-pause6h' : TT('Pause for 6 hours'),
    'Plush-pauseForPrompt' : TT('Pause for how many minutes?'),
    'Plush-pauseFor' : TT('Pause for...'),
    'Plush-multiOperations' : TT('Multi-Operations'),
    'Plush-onQueueFinish' : TT('On Finish'),
    'Plush-sort' : TT('Sort'),
    'Plush-sortAgeAsc' : TT('Sort by Age <small>(Oldest&rarr;Newest)</small>'),
    'Plush-sortAgeDesc' : TT('Sort by Age <small>(Newest&rarr;Oldest)</small>'),
    'Plush-sortNameAsc' : TT('Sort by Name <small>(A&rarr;Z)</small>'),
    'Plush-sortNameDesc' : TT('Sort by Name <small>(Z&rarr;A)</small>'),
    'Plush-sortSizeAsc' : TT('Sort by Size <small>(Smallest&rarr;Largest)</small>'),
    'Plush-sortSizeDesc' : TT('Sort by Size <small>(Largest&rarr;Smallest)</small>'),
    'Plush-confirmPurgeQ' : TT('Purge the Queue?'),
    'Plush-purge' : TT('Purge'),
    'Plush-left' : TT('left'),
    'Plush-maxSpeed' : TT('Max Speed'),
    'Plush-nzo-range' : TT('Range'),
    'Plush-reset' : TT('Reset'),
    'Plush-applySelected' : TT('Apply to Selected'),
    'Plush-page' : TT('page'),
    'Plush-everything' : TT('Everything'),
    'Plush-disabled' : TT('Disabled'),
    'Plush-refreshRate' : TT('Refresh Rate'),
    'Plush-containerWidth' : TT('Container Width'),
    'Plush-confirmDeleteQueue' : TT('Confirm Queue Deletions'),
    'Plush-confirmDeleteHistory' : TT('Confirm History Deletions'),
    'Plush-explain-blockRefresh' : TT('This will prevent refreshing content when your mouse cursor is hovering over the queue.'),
    'Plush-blockRefresh' : TT('Block Refreshes on Hover'),
    'Plush-fetch' : TT('Fetch'),
    'Plush-uploadTip' : TT('Upload: .nzb .rar .zip .gz'),
    'Plush-addnzb-filename' : TT('Optionally specify a filename'),
    'Plush-progress' : TT('Progress'),
    'Plush-remaining' : TT('Remaining'),
    'Plush-notEnoughSpace' : TT('Not enough disk space to complete downloads!'),
    'Plush-freeSpace' : TT('Free Space'),
    'Plush-freeSpaceTemp' : TT('Free (Temp)'),
    'Plush-idle' : TT('IDLE'),
    'Plush-downloads' : TT('Downloads'),

#smpl skin
    'smpl-hourmin' : TT('Hour:Min'),
    'smpl-purgehist' : TT('Delete Completed'),
    'smpl-purgefailhistOK?' : TT('Delete the all failed items from the history?'),
    'smpl-purgefailhist' : TT('Delete Failed'),
    'smpl-links' : TT('Links'),
    'smpl-size' : TT('Size'),
    'smpl-path' : TT('Path'),
    'smpl-numresults@3' : TT('Showing %s to %s out of %s results'),
    'smpl-noresult' : TT('No results'),
    'smpl-oneresult' : TT('Showing one result'),
    'smpl-first' : TT('First'),
    'smpl-previous' : TT('Prev'),
    'smpl-next' : TT('Next'),
    'smpl-last' : TT('Last'),
    'smpl-pauseForPrompt' : TT('Pause for how many minutes?'),
    'smpl-paused' : TT('Paused'),
    'smpl-downloading' : TT('Downloading'),
    'smpl-idle' : TT('Idle'),
    'smpl-emailsent' : TT('Email Sent!'),
    'smpl-saving' : TT('Saving..'),
    'smpl-saved' : TT('Saved'),
    'smpl-failed' : TT('Failed'),
    'smpl-speed' : TT('Speed'),
    'smpl-toggleadd' : TT('Toggle Add NZB'),
    'smpl-dualView1' : TT('DualView1'),
    'smpl-dualView2' : TT('DualView2'),
    'smpl-warnings' : TT('Warnings'),
    'smpl-custom' : TT('Custom'),
    'smpl-getbookmarks' : TT('Get Bookmarks'),
    'smpl-restartOK?' : TT('Are you sure you want to restart SABnzbd?'),
    'smpl-refreshr' : TT('Refresh rate'),
    'smpl-purgeQueue' : TT('Delete All'),
    'smpl-hideEdit' : TT('Hide Edit Options'),
    'smpl-showEdit' : TT('Show Edit Options'),
    'smpl-edit' : TT('Edit'),
    'smpl-progress' : TT('Progress'),
    'smpl-timeleft' : TT('Timeleft'),
    'smpl-age' : TT('Age'),

#Wizard
    'wizard-quickstart' :  TT('SABnzbd Quick-Start Wizard'),
    'wizard-version' :  TT('SABnzbd Version'),
    'wizard-previous' :  TT('Previous'),
    'wizard-next' :  TT('Next'),
    'wizard-zoom' :  TT('Zoom'),
    'wizard-skin' :  TT('Skin'),
    'wizard-explain-skin' :  TT('Which skin would you like to use for SABnzbd?'),
    'wizard-access' :  TT('Access'),
    'wizard-access-anypc' :  TT('I want SABnzbd to be viewable by any pc on my network.'),
    'wizard-access-mypc' :  TT('I want SABnzbd to be viewable from my pc only.'),
    'wizard-access-pass' :  TT('Password protect access to SABnzbd (recommended)'),
    'wizard-access-https' :  TT('Enable HTTPS access to SABnzbd.'),
    'wizard-misc' :  TT('Misc'),
    'wizard-misc-browser' :  TT('Launch my internet browser with the SABnzbd page when the program starts.'),
    'wizard-server' :  TT('Server Details'),
    'wizard-explain-server' :  TT('Please enter in the details of your primary usenet provider.'),
    'wizard-server-help' :  TT('Help'),
    'wizard-server-help1' :  TT('In order to download from usenet you will require access to a provider. Your ISP may provide you with access, however a premium provider is recommended.'),
    'wizard-server-help2' :  TT('Don\'t have a usenet provider? We recommend trying %s.'),
    'wizard-server-con-explain' :  TT('The number of connections allowed by your provider'),
    'wizard-server-ssl-explain' :  TT('Select only if your provider allows SSL connections.'),
    'wizard-server-text' :  TT('Click to test the entered details.'),
    'wizard-server-required' :  TT('This field is required.'),
    'wizard-server-number' :  TT('Please enter a whole number.'),
    'wizard-index-explain' :  TT('If you are a member of newzbin or nzbmatrix, you may enter your username and password here so we can fetch their nzb\'s. This stage can be skipped if you don\'t use either services.'),
    'wizard-index-bookmark' :  TT('Automatically download bookmarked posts.'),
    'wizard-optional' :  TT('Optional'),
    'wizard-example' :  TT('E.g.'),
    'wizard-button-testServer' :  TT('Test Server'),
    'wizard-restarting' :  TT('Restarting SABnzbd...'),
    'wizard-complete' :  TT('Setup is now complete!'),
    'wizard-tip1' :  TT('SABnzbd will now be running in the background.'),
    'wizard-tip2' :  TT('Closing any browser windows/tabs will NOT close SABnzbd.'),
    'wizard-tip3' :  TT('After SABnzbd has finished restarting you will be able to access it at the following location: %s'),
    'wizard-tip4' :  TT('It is recommended you right click and bookmark this location and use this bookmark to access SABnzbd when it is running in the background.'),
    'wizard-tip-wiki' :  TT('Further help can be found on our'),
    'wizard-goto' :  TT('Go to SABnzbd'),
    'wizard-step-one' :  TT('Step One'),
    'wizard-step-two' :  TT('Step Two'),
    'wizard-step-three' :  TT('Step Three'),
    'wizard-step-four' :  TT('Step Four'),
    'wizard-step-five' :  TT('Step Five'),

#Special
    'yourRights' : TT('''
SABnzbd comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it under certain conditions.
It is licensed under the GNU GENERAL PUBLIC LICENSE Version 2 or (at your option) any later version.
''')
    }
