Enable vsphere serial port to telnet.
 To configure the serial port connection for a VM:

    1.In the left navigation pane, select the ESXi server and click the Configuration tab.
    2.Select Security Profile and click Properties next to Firewall.
    3.In the Firewall Properties dialog box, select the VM serial port connected over network box and click 
    4.In the left navigation pane, select the VM and and right-click Edit Settings to display the Virtual Machine Properties window. In the Hardware tab of the Virtual Machine Properties window, click Add. The Add Hardware wizard is displayed.

    5.For Device Type, select Serial Port and click Next.

    For Select Port Type, select the Connect via Network button and click Next.
For Select Network Backing, select the Server button and specify the port number in the Port URI text box in the format telnet://:port-number (for example, telnet://:8601). Click Next.

LINK:
 https://www.juniper.net/documentation/en_US/vmx15.1f4/topics/task/configuration/vmx-vm-connecting-vmware.html