smoothstep:la fonction borne x à 0 en min et 1 en max, puis elle interpole de manière douce entre 0 et 1

interpolation de l'hermite:
equivalent à :  
 t = clamp((x - edge0) / (edge1 - edge0), 0.0, 1.0);
return t \* t \* (3.0 - 2.0 \* t);

fonction qui interpole de 0 à 1 de manière douce entre edge0 et edge1 la fonction x

https://graphtoy.com/

https://lygia.xyz/

## Color mixing

color vec3 is represented as rgb

magenta = yellow.rbg; # equivalent to magenta.r=yellow.r, magenta.g=yellow.b, magenta.b=yellow.g

mix(magenta, yellow, 0.5) # mix 50% of magenta and 50% of yellow
