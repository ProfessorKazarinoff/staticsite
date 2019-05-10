Title: Ryzen 5 Linux PC Build
Date: 2019-05-10 09:21
Modified: 2019-05-10 09:21
Status: draft
Category: diy
Tags: python, IoT, django, server, sensor
Slug: ryzen5-linux-pc-build
Authors: Peter D. Kazarinoff

In this post, I am going to build a Linux PC from parts I ordered from Amazon. This is a Ryzen 5 2400G based build and will be used for general productivity tasks and building projects that require a Linux system. 

[TOC]

## Why am I building a new Linux PC?

I use a couple different computers to write this blog, write my book, and work on Python projects. Below is a partial list:

 * Windows 10 desktop at work
 * Windows 10 laptop at home
 * MacBook Air at home
 * Chromebook at home
 * Linux desktop at home

The computer that is on the fritz right now is the Linux desktop in my home office. I use this computer for writing and general Python programming. In particular, I use the Linux desktop to build software, such as building a custom MicroPython firmware or building Python from source. It is useful to have a Linux system around for these sorts of tasks.

## Parts List

Below is a table of the parts I'm using for the build.

| Component | Part | Link |
| --- | --- |
| processor | AMD Ryzen 5 2400G | [amzn.to/2VyVqyB](https://amzn.to/2VyVqyB) |
| motherboard | MSI B450I Mini-ITX Gaming Plus AC | [amzn.to/2Vzhuco](https://amzn.to/2Vzhuco) |
| hard drive | Crucial P1 1TB M.2 NVMe SSD | [amzn.to/2WEup9e](https://amzn.to/2WEup9e) |
| RAM | Corsair Vengeance DDR4 3000 MHz 16GB (2x8GB) | [amzn.to/2WzXsLh](https://amzn.to/2WzXsLh)  |
| power supply | old Antec 250W SFX PSU that came with the case | (no longer available) |
| case | old Mini-ITX case with included 150W power supply| (no longer available) |

The following is an overview of each component

### AMD Ryzen 5 2400G

The AMD Ryzen 5 2400G is an integrated CPU and GPU in one package (called an APU). I like this processor for the price, the integrated GPU, thread count and speed. My old processor was a couple generations old Intel Core i3 that only had two cores. The Ryzen 5 2400G will be a nice step up.  I chose a Ryzen 5 APU because I did not want to buy a stand alone graphics card. This Linux PC will not be used for gaming or heavy video editing, so I don't need a lot of graphics power. What I do want is a build that is simple (less components), reasonably fast, and low cost. The Ryzen 5 APU fits these requirements nicely. I will only need one CPU cooler and one CPU power supply cable to hook the processor up to the motherboard. Less fans, less cable management, less components in a small case. I think the Ryzen 5 2400G is a win.

### MSI B450I Mini-ITX Gaming Plus AC

The mother board I choose is the MSI B450I Mini-ITX Gaming Plus AC. This motherboard has an AM4 CPU socket for the Ryzen 5 processor I chose. I like the newer B450 chipset, and I hopefully won't need to use an older Ryzen first gen processor to get the system started, which might be required if an older motherboard was employed. The MSI B450I Mini-ITX motherboard has an M.2 slot for my SSD and an HDMI port for monitor output. When using the Ryzen 5 2400G, you need to make sure that the motherboard as an AM4 socket and an HDMI out. This motherboard fits the bill.

### Crucial P1 1TB M.2 NVMe SSD

I picked the Crucial P1 1TB M.2 NVMe SSD for this Linux PC build. The SSD was a component I had trouble deciding on. The current system has a 60GB SSD and a 1TB spinning hard drive. This was a cheap way to equip the system. The problem I have with it is that there have to be two SATA data cables and two SATA power cables, plus the drives need to be mounted in the case. I wanted to keep this build simple and clutter-free. An M.2 form factor drive does not require any cables. M.2 drives plug directly into the motherboard. The Crucial P1 drive I selected is 80 mm long, which is the most common M.2 length. The MSI motherboard I picked has one M.2 slot on the back that the drive will plug into. I choose 1GB of capacity because I just feel like you always need more storage. The old system started with 60GB about 8 years ago and then I had to add a 1TB hard disk because I ran out of space. I want this build to last at least 5 years, so I splurged on extra capacity. I also went with a drive that runs the super fast NMV3e PCIe communication standard. Using an NVMe drive probably won't have any practical performance benefits for the things I will use the new PC for, but I guess I just like to know that I have really fast storage. Long boot times also bug me. Hopefully the new system will boot quickly with the SSD I choose.

### Corsair Vengeance DDR4 3000 MHz 16GB (2x8GB)

I choose 16 GB of DDR4 RAM for my new system. The Corsair Vengeance DDR4 3000 MHz kit I bought includes 2 x 8 GB dimms. I don't know if my system will be able to take advantage of the 3000 MHz maxium clock speed. 

### Old Case and Power Supply

I am going to re-use my old case and power supply from the previous build. It has USB ports and a headphone jack on the front. It worked OK for my old system. The problems with the case that cropped up are that the headphone jack in the front doesn't realy work, and I am concerned about airflow through the case. The CPU fan and GPU fan of my old system were loud and seemed to work really hard on startup and when doing a demanding tasks.

The power supply that I'm going to use came bundled with my old case. It is about 250 watts and conforms to the small SFX form factor. The old power supply has cables for the motherboard, CPU, and hard drives. For this build I am only going to need the cable for the motherboard power and the cable for the CPU power. The leftover extra cables will have to be tucked out of the way

## Build

I built the PC in a couple of steps. First I built the PCC on top of the motherboard box outside of the case to make sure all the components worked together. I plugged in the power supply (power off) and attached an ESD wrist strap to the grounded power supply case.

### Mount the CPU on the motherboard

First I mounted the CPU to the motherboard. Make sure to line up the little triangle on the corner of the CPU with the little corner on the CPU socket on the motherboard. You don't need to push the processor into the socket. The little lever on the side of the socket seats the CPU with the right amount of pressure.

### Mount the RAM on the motherboard

Next, I attached the RAM to the motherboard. There are two clips on the side of the RAM slots of the motherboard. Then I pushed the RAM in until it "clicked"

### Add the CPU cooler

The Ryzen 5 2400G CPU comes with a CPU cooler in the box. The included cooler has thermal paste pre-applied, so no thermal paste needs to be added to the top of the processor before the cooler is mounted. There is a plastic bracket on either side of the motherboard that needs to be removed before the CPU cooler is screwed it. When the plastic brackets come off, the plate on the back of the motherboard falls off. Make sure that plate on the back of the motherboard is aligned when the cooler is screwed in.

I put the cooler on top of the processor and just seated the screws before I tightened it down. I used a cross pattern and tighted each screw about a turn at a time until the cooler was screwed down tight.

### Attach the M.2 SSD drive

Next I flipped the motherboard over and attached the M.2 SSD. There is a baggie that came with the motherboard with a tiny M.2 standoff and a tiny M.2 screw. The standoff goes below the drive and the screw goes above the drive. I slid the drive into the M.2 slot at about a 30 degree angle and tightend it down to the tiny standoff.

### Attach the motherboard power and CPU power. 

Finally, I attached the big 24 pin motherboard power cable from the power supply and the 6 pin supplemental CPU power cable from the power supply. I don't need any other power cables because the SSD is powered by the M.2 slot and the "graphics card" is integrated into the CPU.

## Start Up

After the system was fully assembled, I plugged in a monitor to the HDMI port and plugged in a mouse and keyboard. I also plugged in an ethernet cable. I could use the motherboard's onboard WiFi, but the wired ethernet will be faster and hopefully won't require any setup. Then I started the system for the first time by shorting the POWER pins on the motherboard with a screw driver. After the power turned on, I hit the DELETE key repeatidly to bring up the motherboard bios.

### Update the motherboard BIOS

I downloaded the latest firmare for my motherboard from the MSI website. The download from MSI was a zip file, and I unzipped it onto a USB thumb drive. Within the motherboard BIOS there is the option to update the BIOS firmare. I selected that option and my USB thumb drive that had the firmare file. Then the system re-started and I went went through the BIOS again.

### Check on system specs in the BIOS

Next I checked my new system's specs in the BIOS. I wanted to make sure the CPU and SSD were recognized. I also enabled RAM speed acceleration. For right now I didn't overclock the CPU. I may do that later if I get a new CPU cooler. 

## Install Linux

With the system still outside the case on the motherboard box, I installed Linux from a USB drive. 

From the BIOS, I powered down the system and inserted a thumbdrive with the Linux .iso image into the motherboard. I selected the newest version of Ubuntu. My hope is that the newest version of Ubuntu (not the long-term release) will play nice with my Ryzen 5 APU. 

When I turned the power back on, I pushed F11 over and over to bring up the boot menu. I selected the USB file with the Linux .iso image on it and started the system for the first time.

The Ubuntu installer takes a while and downloads a bunch of stuff while it is installing. The total install time was around 20 minutes.

## Try it out!

## Put the system in the case

Finally I put my new system in my old case. The mother board gets screwed into the four standoffs. A problem I ran into  is that the AMD wraith CPU cooler bumbs into a hard drive caddy on my case. I took a drill bit to the rivets that held the hard drive cady in place and pulled out the sheet metal. This gave me room for my new AMD CPU cooler. 

I just love the fact that there is only one fan and just two power cables to make my system work. The inside of the case is clean and un-cluttered.

## Summary

In this post, I reviewed how I built my new Linux PC from parts I ordered on Amazon. The build was relatively free of hickups. The hardest part was removing the hard drive cady in the case so that my CPU cooler would fit. I do have some upgrades in mind for this system. A new case would be nice. I would like at least one system fan to suplement the CPU cooler. Also a working front audio connection would be great. If I end up overclocking the system, a new CPU cooler is in order. I would also like to get a modular or semi-modular power supply, so there are no extra cables to tie up on the inside of the case.
