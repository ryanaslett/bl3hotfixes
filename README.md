BL3 Hotfix Archive
==================

This is an archive of the hotfixes which are being sent to Borderlands 3.
The first hotfix data was manually collected on September 21, 2019, and
the next few after that were collected manually as well.  Starting on
October 1, 2019, this project was created to check the hotfix data every
hour and write out the hotfixes automatically.

The hotfixes are written twice: once to a brand-new file which includes
a datestamp, stored in the `point_in_time` directory, and once to
`hotfixes_current.json`.

The script which does this is written in Python 3, and should run anywhere
Python does, though you'll need to edit `output_dir` inside the script
itself to have it save out files properly.  Check `requirements.txt` inside
the script dir for the extra Python modules needed for it to run.

All code in this project is is licensed under the
[New/Modified (3-Clause) BSD License](https://opensource.org/licenses/BSD-3-Clause).
A copy can be found in [COPYING.txt](COPYING.txt).

I've also put up a Google Sheets page which has the *all* of the hotfixes
which have been used by GBX (including ones which are no longer active)
up here: [Combined Hotfixes](https://drive.google.com/open?id=1kfkC2hJs0hZSr12bvrQlY0GyEH4S_KAI_xIAqnGmKnQ).  That sheet has all the fields split out
properly into columns, which can make hotfix investigation a lot easier.

Details
=======

(I'm numbering hotfixes and patches here based on what's officially announced
in the "News" section at borderlands.com, though there have been plenty of
smaller hotfixes/patches which haven't been announced in that area.  Often
it'll just be a tweet, or in a few cases a silent update without any
announcement at all.  A bit silly to keep numbering them, really, but I suppose
I'll continue regardless...)

* **2019-09-13**: Borderlands 3 Initial Release (build version `
  OAK-PADDIESEL1-39-CL-2005984`, reported version `1.0.0 CL 2005984` -
  *confirmation needed for reported version*)
* **2019-09-19**: First announced hotfixes, manually collected on the
  21st.  It's possible there were hotfixes active before this point, but
  these are the first we know of.
  ([GBX Post](https://borderlands.com/en-US/news/2019-09-19-borderlands-3-hot-fixes-sept-19/),
  [Local Post Archive](gbx_info_archive/2019-09-19-hotfixes.md))
* **2019-09-26**: First BL3 patch (build version
  `OAK-PATCHDIESEL-11-CL-2015653`, reported version `1.0.1 CL 2015653`
  *(confirmation needed for reported version)*)
  ([GBX Post](https://borderlands.com/en-US/news/2019-09-26-borderlands-3-patch-sept-26/),
  [Local Post Archive](gbx_info_archive/2019-09-26-patch.md))
* **2019-09-27**: Second announced hotfixes, manually collected on the 27th.
  ([GBX Post](https://borderlands.com/en-US/news/2019-09-27-borderlands-3-hot-fixes-sept-27/),
  [Local Post Archive](gbx_info_archive/2019-09-27-hotfixes.md))
* **2019-10-01**: Week 1 of the Borderlands 10-Year Anniversary Celebration
  begins, with "Boss Week," which increases chances for various bosses to
  drop specific legendary gear.  Manually collected one last time -- any
  hotfixes after this point should be grabbed automatically by this process.
  ([GBX Post](https://borderlands.com/en-US/news/2019-10-01-borderlands-anniversary-celebration/),
  [Local Post Archive](gbx_info_archive/2019-10-01-anniversary_1.md))
* **2019-10-03**: Third announced hotfixes, and second patch (build version
  `OAK-PATCHDIESEL-21-CL-2022342`, reported version `1.0.2 CL 2022342`).
  ([GBX Post](https://borderlands.com/en-US/news/2019-10-03-borderlands-3-patch-hotfixes-oct-3/),
  [Local Post Archive](gbx_info_archive/2019-10-03-patch-and-hotfixes.md))
* **2019-10-05**: Unannounced hotfixes which tweak some level geometry in
  a couple of boss areas, seemingly.
* **2019-10-08**: Week 2 of the Borderlands 10-Year Anniversary Celebration,
  with "Rare Spawn Hunt", after a period of time where Week 1 was disabled but
  Week 2 wasn't active yet.
  ([GBX Post](https://borderlands.com/en-US/news/2019-10-07-borderlands-3-rare-spawn-hunt/),
  [Local Post Archive](gbx_info_archive/2019-10-07-anniversary_2.md))
* **2019-10-10**: Fourth announced hotfixes
  ([GBX Post](https://borderlands.com/en-US/news/2019-10-10-borderlands-3-hotfixes-oct-10/),
  [Local Post Archive](gbx_info_archive/2019-10-10-hotfixes.md))
* **2019-10-15**: Week 3 of the Borderlands 10-Year Anniversary Celebration,
  with "Show Me the Eridium."  A couple of the statements have errors, perhaps
  those will get fixed up eventually.  (They didn't. :)
  ([GBX Post](https://borderlands.com/en-US/news/2019-10-14-borderlands-3-show-me-the-eridium/),
  [Local Post Archive](gbx_info_archive/2019-10-14-anniversary_3.md))
* **2019-10-17**: Fifth announced hotfixes
  ([GBX Post](https://borderlands.com/en-US/news/2019-10-17-borderlands-3-hotfixes-oct-17/),
  [Local Post Archive](gbx_info_archive/2019-10-17-hotfixes.md))
* **2019-10-22**: Week 4 of the Borderlands 10-Year Anniversary Celebration,
  with "Mayhem on Twitch."
  ([GBX Post](https://borderlands.com/en-US/news/2019-10-22-borderlands-3-mayhem-on-twitch/),
  [Local Post Archive](gbx_info_archive/2019-10-22-anniversary_4.md))
* **2019-10-24**: Sixth announced hotfixes, third patch (build version
  `OAK-PATCHDIESEL-45-CL-2038940`, reported version `1.0.3 CL 2038940`),
  and activation of the Bloody Harvest event
  ([Day-of GBX Post](https://borderlands.com/en-US/news/2019-10-24-borderlands-3-patch-hotfixes-roadmap-oct-24/),
  [Local Post Archive](gbx_info_archive/2019-10-24-patch_and_hotfixes.md),
  [Event Details GBX Post](https://borderlands.com/en-US/news/2019-10-21-bloody-harvest-trailer-info/),
  [Local Post Archive](gbx_info_archive/2019-10-21-bloody_harvest_trailer.md))
  * A very small second hotfix update was applied a few hours later, related to
    Twitch chest interactions (just one additional hotfix)
* **2019-10-25**: Small hotfix update to tweak Captain Haunt slightly (increased
  volume and better loot drops)
  ([GBX Tweet](https://twitter.com/GearboxOfficial/status/1187898114935590913),
  [Local Archive](gbx_info_archive/2019-10-25-captain_haunt_tweak.md))
* **2019-10-29**: Week 4 hotfixes were partially removed (namely Twitch
  interaction and Mayhem XP buffs).  The rest of Week 4 is being left in as
  permanent changes.
* **2019-10-31**: Seventh announced hotfixes.
  ([GBX Post](https://borderlands.com/en-US/news/2019-10-31-borderlands-3-hotfixes-oct-31/),
  [Local Post Archive](gbx_info_archive/2019-10-31-hotfixes.md))
* **2019-11-01**: Halloween-specific hotfix to have 100% haunted enemies was
  removed.
* **2019-11-07**: Eighth announced hotfixes.
  ([GBX Post](https://borderlands.com/en-US/news/2019-11-07-borderlands-3-hotfixes-nov-7/),
  [Local Post Archive](gbx_info_archive/2019-11-07-hotfixes.md))
* **2019-11-14**: Ninth announced hotfixes.
  ([GBX Post](https://borderlands.com/en-US/news/2019-11-14-borderlands-3-hotfixes-nov-14),
  [Local Post Archive](gbx_info_archive/2019-11-14-hotfixes.md))
  * An unannounced update a few hours after that got rid of a couple of
    hotfixes.
* **2019-11-21**: Tenth announced hotfixes, fourth official patch (build
  version `OAK-PATCHDIESEL-71-CL2060134`, reported version `1.0.4 CL 2060134`),
  and release of Takedown at Maliwan's Blacksite.  Nearly half of the
  previously-established hotfixes have been removed, presumably because
  they're now baked into the game data.  A few hours later, some newer
  hotfixes were added to the mix.
  ([GBX Post](https://borderlands.com/en-US/news/2019-11-21-borderlands-3-patch-hotfixes-nov-21/),
  [Local Post Archive](gbx_info_archive/2019-11-21-patch_and_hotfixes.md))
* **2019-11-22**: Small hotfix update to revert a change to Megavore which was
  having unintended consequences.  Also seems to add in some sniper rifle buffs
  which had been removed with yesterday's update.
  ([GBX Tweet](https://twitter.com/GearboxOfficial/status/1198014507991224320),
  [Local Archive](gbx_info_archive/2019-11-22-megavore_revert.md))
* **2019-11-26**: Eleventh announced hotfixes, just a quick fix to the Butcher.
  ([GBX Post](https://borderlands.com/en-US/news/2019-11-26-borderlands-3-hotfixes-nov-26/),
  [Local Archive](gbx_info_archive/2019-11-26-hotfixes.md))
* **2019-12-05**: Twelfth announced hotfixes, including disabling the Bloody
  Harvest event.
  ([GBX Post](https://borderlands.com/en-US/news/2019-12-05-borderlands-3-hotfixes-dec-5/),
  [Local Archive](gbx_info_archive/2019-12-05-hotfixes.md))
* **2019-12-10**: Unannounced patch to the game EXE, it seems (build version
  seems to have remained `OAK-PATCHDIESEL-71-CL2060134`, but the reported
  version is now `1.0.4 CL 2060135`)
* **2019-12-12**: Fifth official patch (build version `OAK-PATCHDIESEL-97-CL2077505`,
  reported version `1.0.5 CL 2077505`), fixing various bugs in the engine and laying
  the groundwork for the upcoming Moxxi Heist DLC.  Also includes the welcome change
  of having a main-menu notification for when hotfixes are loaded!
  ([GBX Post](https://borderlands.com/en-US/news/2019-12-12-borderlands-3-patch-dec-12/),
  [Local Archive](gbx_info_archive/2019-12-12-patch.md))
  Additionally, there were three smallish hotfix updates throughout the day, which
  were mostly just minor cleanup stuff, though the last of them buffed the droprates
  of rare spawns, trial bosses, and slaughter bosses.
  ([GBX Tweet](https://twitter.com/Borderlands/status/1205217625959096320),
  [Local Archive](gbx_info_archive/2019-12-12-tweet.md))
* **2019-12-13**: Small hotfix update which tweaks the R4kk P4ck COM, and fixes
  Zane's barrier in a couple of situations.
  ([GBX Tweet](https://twitter.com/Borderlands/status/1205669994807250944),
  [Local Archive](gbx_info_archive/2019-12-13-tweet.md))
* **2019-12-19**: Release of DLC1 (Moxxi's Heist of the Handsome Jackpot), minor
  patch (build version `OAK-PATCHDIESEL-99-CL2079527`, reported version `1.0.5 CL 2079527`),
  and the thirteenth announced hotfix updates.
  ([GBX Post](https://borderlands.com/en-US/news/2019-12-19-borderlands-3-hotfixes-dec-19/),
  [Local Archive](gbx_info_archive/2019-12-19-hotfixes_and_dlc1.md))
* **2020-01-02**: Hotfixes updated to remove Christmas-themed main menu.
* **2020-01-09**: Fourteenth announced hotfixes, just tweaking a few minor things.
  ([GBX Post](https://borderlands.com/en-US/news/2020-01-09-borderlands-3-hotfixes-jan-9/),
  [Local Archive](gbx_info_archive/2020-01-09-hotfixes.md))
* **2020-01-16**: Fifteenth announced hotfixes, including the Farming Frenzy
  event and temporary scaling changes to the Maliwan Takedown.  A minor
  hotfix update later in the day cleaned up some duplicate statements.
  ([GBX Post](https://borderlands.com/en-US/news/2020-01-16-borderlands-3-hotfixes-jan-16/),
  [Local Archive](gbx_info_archive/2020-01-16-hotfixes.md) -
  [Farming Frenzy Post](https://borderlands.com/en-US/news/2020-01-15-borderlands-3-farming-frenzy/),
  [Local Archive](gbx_info_archive/2020-01-15-farming_frenzy.md))
* **2020-01-17**: A small hotfix update to tweak Urist Enforcer's drop rate
  a bit, though earlier hotfixes still in the file might mean the buff isn't
  applying.  Also the tweet from GBX implies that it was supposed to have
  buffed a bunch of other enemy drops as well, which it doesn't actually do.
  ([GBX Tweet](https://twitter.com/GearboxOfficial/status/1218233115296124936),
  [Local Archive](gbx_info_archive/2020-01-17-tweet.md))
* **2020-01-23**: Sixteenth announced hofixes, just various bugfixes and
  balance changes.
  ([GBX Post](https://borderlands.com/en-US/news/2020-01-23-borderlands-3-hotfixes-jan-23/),
  [Local Archive](gbx_info_archive/2020-01-23-hotfixes.md))
* **2020-01-30**: Seventeenth announced hotfixes, and introduction of Rare Chest
  Riches event.  Farming Frenzy event will apparently remain active permanently.
  ([GBX Post](https://borderlands.com/en-US/news/2020-01-30-borderlands-3-hotfixes-jan-30/),
  [Local Archive](gbx_info_archive/2020-01-30-rare_chest_riches.md))
* **2020-02-04**: A small unannounced hotfix update which tweaks Cistern of
  Slaughter, presumably just bugfixes.
* **2020-02-05**: Another small unannounced hotfix which nerfs some of the 40% drop rates
  introduced in the Farming Frenzy event down to 30%.
* **2020-02-13**: Sixth official patch (build version `OAK-PATCHDIESEL0-45-CL2109921`,
  reported version `1.0.6 CL 2109921`), eighteenth announced hotfixes, and introduction of
  Broken Hearts timed content update.  Level cap increase to 53, among other changes.
  ([GBX Post](https://borderlands.com/en-US/news/2020-02-13-borderlands-3-patch-hotfixes-feb-13/),
  [Local Archive](gbx_info_archive/2020-02-13-patch_hotfixes_broken_hearts.md))
  * A small hotfix update a few hours later disabled the Rare Chest Riches event.
* **2020-02-20**: Nineteenth announced hotfixes, and deactivation of Broken Hearts
  event.
  ([GBX Post](https://borderlands.com/en-US/news/2020-02-20-borderlands-3-hotfixes-feb-20/),
  [Local Archive](gbx_info_archive/2020-02-20-hotfixes.md))
  * A small hotfix update afterwards removed a few Broken Hearts-specific balance changes
    which were missed on the initial update.

