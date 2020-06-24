Title: Ryzen 5 Linux PC Build
Date: 2019-05-10 09:21
Modified: 2019-05-10 09:21
Status: draft
Category: diy
Tags: hardware, diy
Slug: ryzen5-linux-pc-build
Authors: Peter D. Kazarinoff

In this post, I am going to describe my PC build. The computer I built runs Linux (Ubuntu 20.04). The parts I used in the build are shown below.

[TOC]

## Why am I building a new Linux PC?

I use a couple different computers to write this blog, write my [book](https://www.amazon.com/Problem-Solving-Python-3-7-open-source/dp/1693405415), and work on [Python projects](https://github.com/ProfessorKazarinoff/). Below is a partial list:

 * Windows 10 desktop at work
 * Windows 10 laptop at home
 * MacBook Air at home
 * Chromebook at home
 * Linux desktop at home

The computer that is on the fritz right now is the Linux desktop in my home office. I use this computer for writing, editing and general Python programming. In particular, I use the Linux desktop to build software, such as building custom MicroPython firmware or building Python from source. It is useful to have a Linux system for these sorts of tasks. I have also stream from this Linux desktop PC as it is the only PC in the house that is connected using hard-wired ethernet.

## Parts List

Below is a table of the parts I'm using for the build.

| Component | Part | Link |
| --- | --- | --- |
| processor | AMD Ryzen 5 2400G | [amzn.to/2VyVqyB](https://amzn.to/2VyVqyB) |
| motherboard | MSI B450I Mini-ITX Gaming Plus AC | [amzn.to/2Vzhuco](https://amzn.to/2Vzhuco) |
| hard drive | Crucial P1 1TB M.2 NVMe SSD | [amzn.to/2WEup9e](https://amzn.to/2WEup9e) |
| RAM | Corsair Vengeance DDR4 3000 MHz 16GB (2x8GB) | [amzn.to/2WzXsLh](https://amzn.to/2WzXsLh)  |
| power supply | Corsair 450SF | (no longer available) |
| case | Silverstone SG13B-V2 | [amazon.com/dp/B00U8IS89E/](https://www.amazon.com/dp/B00U8IS89E/) |

The following is an overview of each component

### AMD Ryzen 5 2400G

The AMD Ryzen 5 2400G is an integrated CPU and GPU in one package (called an APU). I like this processor for the price, the integrated GPU, thread count and speed. My old processor was a couple generations old Intel Core i3 that only had two cores. The Ryzen 5 2400G will be a nice step up.  I chose a Ryzen 5 APU because I did not want to buy a stand-alone graphics card. This Linux PC will not be used for gaming or heavy video editing, so I don't need a lot of graphics power. What I do want is a build that is simple (less components), reasonably fast, and low cost. The Ryzen 5 APU fits these requirements nicely. I will only need one CPU cooler and one CPU power supply cable to hook the processor up to the motherboard. Less fans, less cable management, less components in a small case. I think the Ryzen 5 2400G is a win.

### MSI B450I Mini-ITX Gaming Plus AC

The mother board I choose is the MSI B450I Mini-ITX Gaming Plus AC. This motherboard has an AM4 CPU socket for the Ryzen 5 processor I chose. I like the newer B450 chipset, and I hopefully won't need to use an older Ryzen first gen processor to get the system started, which might be required if an older motherboard was employed. The MSI B450I Mini-ITX motherboard has an M.2 slot for an SSD and an HDMI port for monitor output. Since I'm using the Ryzen 5 2400G (without a discrete graphics card), I needed to make sure that the motherboard as an AM4 socket and has an HDMI out. This motherboard fits the bill.

### Crucial P1 1TB M.2 NVMe SSD

I picked the Crucial P1 1TB M.2 NVMe SSD for this Linux PC build. The SSD was a component I had trouble deciding on. My old system has a 60GB SSD and a 1TB spinning hard drive. This was a cheap way to equip the system. The problem I had with it is that there had to be two SATA data cables and two SATA power cables, plus two drives needed to be mounted in the case.

I wanted to keep this build simple and clutter-free. M.2 drives plug directly into the motherboard and do not require any cables. The Crucial P1 drive I selected is 80 mm long, which is the most common M.2 length. The MSI motherboard I picked has one M.2 slot on the back that the drive plugs into. I choose 1GB of capacity because I just feel like **you always need more storage**.

The old system started out with a 60GB SSD about 8 years ago. Then I added a 1TB spinning hard disk because I ran out of storage space. I want this build to last at least 5 years, so I splurged on extra SSD capacity. I also went with a drive that runs the super fast NMV3e PCIe communication standard. An NVMe SSD drive probably won't have any practical performance benefits compared to a SATA SSD for the things I use the new PC for; but I guess I just like to know that I have really fast storage. Plus, long boot times bug me.

### Corsair Vengeance DDR4 3000 MHz 16GB (2x8GB)

I choose 16 GB of DDR4 RAM for my new system. The Corsair Vengeance DDR4 3000 MHz kit I bought includes 2 x 8 GB dimms. I don't know if my system will be able to take advantage of the 3000 MHz maxium clock speed. It's really just 16 GB of standard DDR4 memory. 

### Power Supply

The power supply I went with this the ...

For this build I am only going to need the cable for the motherboard power and the cable for the CPU power. These cables are built into the power supply. The other modular cables aren't needed.

### Case

I put all the components inside the Silverstone SG13B-V2 Mini ITX case. This case accepts mini ITX motherboards and can accomodate standard ATX powersuplies (as well as smaller SFX power supplies). It isn't fancy, but it is inexpensive and gets the job done.

### Fan

I bought a fan for the SilverStone case becuase it doesn't come with one. I mounted the fan in the front of the case.

## Build

I built the PC in a couple of steps. First I built the PCC on top of the motherboard box outside of the case to make sure all the components worked together. 

Before I started building, I plugged in the power supply (power off) and attached an ESD wrist strap to the grounded power supply case with the aligator clip.

### Mount the CPU on the motherboard

Next, I installed the CPU in the motherboard. Make sure to line up the little triangle on the corner of the CPU with the little corner on the CPU socket on the motherboard. You don't need to _push_ the processor into the socket. The little lever on the side of the socket seats the CPU with the right amount of pressure.

### Mount the RAM on the motherboard

Next, I attached the RAM to the motherboard. There are two clips on the side of the RAM slots of the motherboard. Then I pushed the RAM in until it "clicked". The RAM only fits into the RAM slots in one orientation.

### Add the CPU cooler

The Ryzen 5 2400G CPU comes with a CPU cooler included in the box. The included cooler has thermal paste pre-applied, so no thermal paste needs to be added to the top of the processor before the cooler is mounted. There are two plastic brackets, one on each side of the processor that need to be removed before the CPU cooler is attached. When the plastic brackets come off, the plate on the back of the motherboard falls off. Make sure that plate on the back of the motherboard is aligned when the cooler is screwed in.

I put the cooler on top of the processor and just seated the screws before I tightened it down. I used a cross pattern and tighted each screw about a turn at a time until the cooler was screwed down tight.

### Attach the M.2 SSD drive

Next, I flipped the motherboard over and attached the M.2 SSD. The baggie of screw that came with the motherboard contained a tiny M.2 standoff and a tiny M.2 screw. The standoff goes "below" the M.2 drive and the little screw goes "above" the M.2 drive. I slid the drive into the M.2 slot at about a 30 degree angle, then pushed it down till hit was horizontal and tightend the end down to the standoff with the tiny screw.

### Attach the motherboard power and CPU power. 

Finally, I attached the big 24 pin motherboard power cable from the power supply and the 6 pin supplemental CPU power cable from the power supply to the motherboard. I don't need any other power cables because the SSD is powered by the M.2 slot and the "graphics card" is integrated into the CPU.

All these steps were accomplished outside the case.

## Start Up

After the system was fully assembled, I plugged a monitor into the HDMI port and plugged a mouse and keyboard into USB ports. I also plugged in an ethernet cable. I could use the motherboard's onboard WiFi, but the wired ethernet is faster and won't require any setup. I started the system for the first time by shorting the POWER pins on the motherboard with a screw driver. After the power turned on, I hit the DELETE key rapidly to bring up the motherboard BIOS.

### Update the motherboard BIOS

I downloaded the latest firmare for my motherboard from the MSI website. The download from MSI was a zip file, and I unzipped it onto a USB thumb drive. Within the motherboard BIOS there is the option to update the BIOS firmare. I selected that option and my USB thumb drive that contained the firmare file. Then the system re-started and I went went into the BIOS again.

### Check the system specs in the BIOS

Next I checked my new system's specs in the BIOS. I wanted to make sure the CPU and SSD were recognized. For right now, I didn't overclock the CPU or the RAM.

## Install Linux

With the system still outside the case and the motherboard sitting on top of the motherboard box, I installed Ubuntu 20.04 from a USB drive. 

From the BIOS, I powered down the system and inserted a thumbdrive with the Linux (Ubuntu 20.04) .iso image into the motherboard. I selected the newest version of Ubuntu. My hope is that the newest version of Ubuntu will play nice with my newer Ryzen 5 APU. 

When I turned the power back on, I pushed F11 over and over to bring up the boot menu. I selected the USB thumb drive with the Linux .iso image on it and started the system for the first time.

The Ubuntu installer takes a while to complete and downloads a bunch of stuff during the installation . The total install time was around 20 minutes.

## Try it out!

After Ubuntu was set up, I tried the new system out. It worked great! Firefox opens quickly and YouTube videos stream no problem. I also entered those standard Linux command line update commands:

```text
sudo apt-get update
sudo apt-get upgrade
```

## Put the system in the case

Finally, I put my new system in the case. The mother board gets screwed into the four motherboard standoffs at the bottom of the case. A problem I ran into is that the AMD wraith CPU cooler bumbs into a hard drive caddy on my case. I took the hard drive caddy off to provide room for the AMD CPU cooler. 

I love the fact the system only contains one fan and two power cables. The inside of the case is clean and un-cluttered.

## Summary

In this post, I reviewed how I built my new Linux PC from individual components. The build was relatively free of hickups. The hardest part was removing the hard drive cady in the case so that the CPU cooler would fit. I do have some upgrades in mind for this system. A fanier case would be nice. If I end up overclocking the system, a new CPU cooler might be in order. And there is always the possiblity to add a discrete graphics card and more powerful CPU. 
