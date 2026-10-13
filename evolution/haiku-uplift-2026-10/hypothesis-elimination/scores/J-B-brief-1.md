Notes (J-B, brief-1)

- E4I: Correct mechanism. Explains how the courier change and cold-hold interact, uses Harbour as the control, and points out that Millbrook has no Tomas. Very actionable: paired recollection with a 0.5 mmol/L threshold, a maximum transit time in the courier contract, and incident handling for the ED visits. It lists normal calcium and sodium as evidence but never says what they rule out, and it misses the argument that inpatient samples on the same lot are unaffected.
- D1K: Correct core with explicit assumptions and a 75% confidence figure. It says that under the 90-minute loop "almost no specimen waited 30 minutes". That doesn't follow, since the average wait was around 45 minutes, and it is an unjustified step in the timing argument. The paired-test design ("fridge, then room temperature") is muddled.
- W2J: The most complete reply. It covers the interaction, Harbour as control, the inpatient and ED samples that run on the same analyzer and lot, the Sept 4 vs Sept 8 lag, Millbrook, a lookback for patient harm, a lab comment and what would change the conclusion. It is a little long, and "Tomas only draws part of Ridgeway's volume" is an assumption it doesn't flag.
- W3T: Strong. It explains why calcium is normal (no EDTA contamination), explicitly treats cold-hold alone as not the change, and names fridge temperature as the next lead. But it invents "roughly 35% of volume" for the other two clinics and says Millbrook has "almost the same flag rate" without any volume data.
- S2R: Correct core but thin. It never uses the fact that Millbrook has no Tomas, or the inpatient/ED contrast. It claims, without flagging, that lithium heparin plasma is "less affected by cold". It proposes narrowing the recall list instead of telling clinicians to repeat the test, and has no patient lookback.
- M6M: Solid. It has the Millbrook argument, the timing lag and good patient-safety steps, including the ~4.5% excess lookback. Item 3 (rerunning on Analyzer A to "clear it") is confused, and so is the closing suggestion about low potassium results.
- O9T: Correct direction, but it says the courier change came "three days before the spike" when the gap is one day (Sept 7 vs Sept 8). It handles the cold-hold/courier interaction weakly, never uses Millbrook as a counter to the Tomas theory, and never says to stop refrigerating potassium samples. The assumptions section is good.
- Q2G: Correct. It has the strong inpatient/same-lot argument and a good paired cold test. It overstates that hemolysis is "ruled out" when 7% of flagged samples are hemolyzed, omits the Millbrook/Tomas argument, and gives no patient-harm lookback or clear trigger that would change the conclusion.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-B,E4I,6,7,6,6,6,7,6,44
J-B,D1K,5,6,5,6,6,7,5,40
J-B,W2J,7,7,6,7,5,7,6,45
J-B,W3T,7,7,5,7,5,7,4,42
J-B,S2R,4,5,4,5,6,7,5,36
J-B,M6M,6,6,5,6,6,7,5,41
J-B,O9T,4,5,4,5,5,7,4,34
J-B,Q2G,5,6,5,5,6,7,5,39
```

```ranking
judge,brief,order
J-B,brief-1,W2J E4I W3T M6M D1K Q2G S2R O9T
```
