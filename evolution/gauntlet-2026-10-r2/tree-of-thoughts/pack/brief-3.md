I lead infrastructure at Sallowfield General Hospital. Our imaging archive holds 420 TB of X-ray, CT and MRI studies and grows by about 150 GB a day. It lives in our basement data centre and is backed up nightly to a tape library in the next room. Last winter a neighbouring hospital lost its data centre to a flood. Our board now wants us able to lose ours to flood or fire and still have radiologists working again, with patients' previous scans available, within 8 hours. They've approved up to €2M over five years and want a recommendation in January.

The options:

- Replicate the archive continuously to Nimbara Cloud and restore from there if we lose the site: about €110k a year. Our CIO likes not having a second building to run.
- Build a standby site in the spare plant room at St Brennan's, our sister hospital 3 km away: €1.1M up front plus €70k a year. Our facilities team is keen because we'd control it.
- Have Tarnwell Continuity host standby servers in their facility 200 km away, kept in sync with ours: €360k a year.
- Keep the tapes but send a set offsite every week: €30k a year.

Background: the hospital's internet connection is a 2 Gbps line, which Nimbara says is plenty for keeping the replica in step. Our archive software comes from Brisewood Imaging, which ships it on its own certified appliances and won't support it on anything else, so our servers are a matched set. St Brennan's is on the same stretch of river as us, and both hospitals ran on generators for four days when the Wharf Road substation flooded in 2024.

Which approach should we take?
