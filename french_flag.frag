#ifdef GL_ES
precision mediump float;
#endif

#define PI 3.14159265359

uniform vec2 u_resolution;
uniform vec2 u_mouse;
uniform float u_time;

vec3 colorA = vec3(0.149, 0.141, 0.912);
vec3 colorB = vec3(1.000, 0.833, 0.224);

float plot(vec2 st, float pct) {
    return smoothstep(pct - 0.01, pct, st.y) -
        smoothstep(pct, pct + 0.01, st.y);
}

void main() {
    vec2 posxy = gl_FragCoord.xy / u_resolution.xy;

    vec3 color = vec3(0.);

    color.r += 1. - step(1. / 3., posxy.x);
    color.rgb += vec3(step(1. / 3., posxy.x) - step(2. / 3., posxy.x));
    color.b += step(2. / 3., posxy.x);

    // Plot transition lines for each channel
    color = mix(color, vec3(1.0, 0.0, 0.0), plot(posxy, color.r));
    color = mix(color, vec3(0.0, 1.0, 0.0), plot(posxy, color.g));
    color = mix(color, vec3(0.0, 0.0, 1.0), plot(posxy, color.b));

    gl_FragColor = vec4(color, 1.0);
}
