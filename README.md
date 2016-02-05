Libcloud examples for StackStorm
=====
![multi-cloud](http://www.cathyfamily.com/media/48831/peanuts.png)

What is multi-cloud?
----
The ability to orchestrate against multiple clouds, public, private, hybrid.

How do I use this pack?
-----

st2 run packs.install packs=libcloud_examples repo_url=https://github.com/tonybaloney/libcloud.extra subtree=true

What is in this pack?
------

## Actions

`deploy_to` - Deploy an image to a particular cloud, choose the cloud as a parameters
`example_parallel_compute` - A mistral workflow that deploys 2 VMs, adds A records to a DNS zone and adds them to a load balancer
![](https://raw.githubusercontent.com/tonybaloney/libcloud.extra/master/screenshots/example_parallel_compute.PNG)
`list_all_vms` - Return a merged list of all the nodes across all configured clouds
![](https://raw.githubusercontent.com/tonybaloney/libcloud.extra/master/screenshots/list_all_vms.PNG
`example_scale_event` - Scale out a cluster by a number of nodes and add them to a load balancer
![](https://raw.githubusercontent.com/tonybaloney/libcloud.extra/master/screenshots/example_scale_event.PNG)
`list_clouds` - List the available clouds for a given type in the libcloud pack

## Chatops aliases

![Alias example](https://raw.githubusercontent.com/tonybaloney/libcloud.extra/master/screenshots/alias_clouds.PNG)

`!allservers {{search=all}}` - Get a list of all the servers (optional filter)
`!clouds {{type=all}}` - List all the clouds
`!deploy_to {{cloud}} {{name}} {{image}} {{size}}` - Deploy a node to a cloud
`!servers {{credentials}}` - List servers in a cloud
`!containers {{credentials}}` - List containers in a cloud
![](https://raw.githubusercontent.com/tonybaloney/libcloud.extra/master/screenshots/list_containers.PNG)
