U7V: Catches the dosing regression, the post-hoc bar change and the author-as-judge problem. It misses that the carprofen question is one of v2.4's own worked examples, and it frames the short answer vaguely. Its uncertainty is well calibrated, and it reads cleanly.

V6Y: Catches everything, including the contamination of the carprofen test by the worked examples, the noise in the clarity margin, and the need for a mechanical frequency check. The "score one dimension at a time" advice is extraneous and reads like method. It states few of its assumptions.

Y9L: Solid on dosing, the bar change and the author bias. It offers a practical ship-Monday fallback (verify every table) and states its assumptions explicitly. It calls the carprofen result a "warning sign" and misses that the question overlaps a worked example.

Q6P: Catches everything, including the carprofen contamination, the noise, the conservative-reading principle and the author's scores. It flags its assumption about length, and its actions are concrete. "Guard dimension" is mild jargon.

```scores
judge,code,V1,V2,V3,V4,G1,G2,G3,total
J-B,U7V,5,5,5,6,6,7,6,40
J-B,V6Y,7,6,6,6,5,6,5,41
J-B,Y9L,5,6,5,7,5,7,6,41
J-B,Q6P,7,6,6,6,6,6,6,43
```

```ranking
judge,brief,order
J-B,brief-1,Q6P V6Y Y9L U7V
```
