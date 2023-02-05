# AutoDogFeeder
Automated dog feeder and notification system for Raspberry Pico W

Primary objectives: 
- [x] Feed the dog on a regular schedule
- [x] Feed the dog an exact and standardized volume of food upon feed time
- [x] Ensure full controll and accessibility to Auto-Feeder settings for the pet-owner
- [x] Ensure stable connections to RestfulAPI and connected systems
- [x] Ensure physical build secures rotating junctions from pinching hands
- [x] Ensure setup is reachable to all users via html setup page

Secondary objectives:
- [x] Provide owners with a easy to use interface available via IOS app
- [x] Provide end - end setup through network configuration via IOS app
- [ ] Create a model that would facilitate standardized food canisters(i.e waterbottles, or any sealable lid with standard threading) (In Progress)
- [ ] Create tamper-proof locking module that secures food container to base
- [ ] Enforce headers in API requests
- [ ] Enforce https on API host
- [ ] Disable AP password ... it's annoying and the communication is limited to AP and Lan; does not touch WAN until after config has been completed with successful Wi-Fi connection
- [x] Design Appicon image

Additional features:
- [ ] "Buddy System": Coordinated feed / water management with water-level monitoring and modular canister design
- [ ] Setup step-by-step for IOS
- [ ] Refine dynamic constraints to work with IPad & Iphone
- [ ] Add "Feed Me" manual feed button to AppleWatch (This had previously been a challenge to do given weird networking characteristics of WatchOS)
- [ ] Expand application to Android / Google
- [ ] Enable twilio account configuration and notification
- [ ] Expand IOS app to include user-feedback for successful field entries and timer updates
- [ ] Enforce a "Submit" button in app to create a cohesive and predictable experience (currently auto-submits upon any changes to time field)
- [ ] "CheeseBall": Future model to handle larger breeds (larger: feed amounts, kibble sizes, enlarged spindle and housing volume, increased servo power)



